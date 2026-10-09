"""Audit command-line entrypoint.

This module runs baseline repository quality checks used by the audit process.
It is designed to run inside the tools uv workspace as a Python monorepo app.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

# Sections every skill file must carry, regardless of specialization. Kept to
# the universal minimum so deliberate per-skill omissions do not false-positive;
# the license/RC block is enforced separately by validate_skill_compliance.
REQUIRED_SECTIONS = (
    "## System Prompt",
    "### Guardrails",
)

# Matches a backticked kebab-case token used in the "`<name>` skill" handoff
# idiom, e.g. "Invoke the `writing-plans` skill" — the shape of a cross-skill
# reference. The captured token must resolve to a skills/<token>.md file.
_SKILL_REF = re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`\s+skill\b")

# Matches a markdown link into the skills/ directory, e.g. (skills/coder.md).
_SKILL_LINK = re.compile(r"\(([^)]*?skills/([a-z0-9-]+)\.md)\)")

# A triggered skill is loaded whole into the agent's context window, so every
# line competes with the conversation. Repository policy caps each skill file,
# frontmatter included, at 100 lines; detail beyond that is cut, not split.
MAX_SKILL_LINES = 100

# Agent Skills frontmatter limits: `name` is lowercase/digits/hyphens, at most
# 64 characters, and must not use reserved words; `description` is at most
# 1024 characters and must not contain XML tags.
_SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MAX_NAME_CHARS = 64
MAX_DESCRIPTION_CHARS = 1024
RESERVED_NAME_WORDS = ("anthropic", "claude")

# The description is all an agent sees when choosing a skill, so it must say
# when to use the skill, not repeat the old generic placeholder.
PLACEHOLDER_DESCRIPTION = "guidance for specialized technical workflows"
TRIGGER_PHRASE = "Use when"

_FRONTMATTER_KEY = re.compile(r"([a-z][a-z0-9_-]*):\s*(.*)")
_BLOCK_SCALAR = re.compile(r"[>|][+-]?")


def parse_frontmatter(content: str) -> dict[str, str] | None:
    """Parse the flat YAML frontmatter subset used by skill files.

    Supports top-level ``key: value`` pairs, optionally quoted, and folded or
    literal block scalars (``>-``, ``|``) whose indented lines are joined with
    spaces. Avoids a YAML dependency; nested mappings are not supported.

    Args:
        content: Full skill file text.

    Returns:
        Mapping of frontmatter keys to string values, or None when the file
        does not open with a ``---`` delimited frontmatter block.
    """
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None

    fields: dict[str, str] = {}
    key: str | None = None
    for line in lines[1:end]:
        if key is not None and (line.startswith((" ", "\t")) or not line.strip()):
            fields[key] = f"{fields[key]} {line.strip()}".strip()
            continue
        key = None
        match = _FRONTMATTER_KEY.fullmatch(line)
        if not match:
            continue
        name, value = match.groups()
        if _BLOCK_SCALAR.fullmatch(value.strip()):
            fields[name] = ""
            key = name
        else:
            fields[name] = value.strip().strip("\"'")
    return fields


def validate_skill_compliance(root: Path) -> int:
    """Validate repository context and license checks exist in all skills.

    Args:
        root: Repository root path.

    Returns:
        Zero when every skill contains required compliance directives.
    """
    required_tokens = (
        "### Repository Context & License Compatibility (Mandatory)",
        "`AGENTS.md`",
        "`CONTRIBUTING.md`",
        "/docs",
        "`CONVENTIONS.md`",
        "`CONTEXT.md`",
        "/LICENSE",
        "compatible",
        "license-check tooling",
    )

    missing_by_file: dict[str, list[str]] = {}
    for skill_file in sorted((root / "skills").glob("*.md")):
        content = skill_file.read_text()
        missing = [token for token in required_tokens if token not in content]
        if missing:
            missing_by_file[str(skill_file.relative_to(root))] = missing

    if not missing_by_file:
        return 0

    for skill_path, missing in missing_by_file.items():
        print(f"[skill-compliance] {skill_path} missing: {', '.join(missing)}")
    return 1


def validate_canonical_sections(root: Path) -> int:
    """Validate every skill file carries the required canonical sections.

    Args:
        root: Repository root path.

    Returns:
        Zero when every skill contains all REQUIRED_SECTIONS.
    """
    missing_by_file: dict[str, list[str]] = {}
    for skill_file in sorted((root / "skills").glob("*.md")):
        content = skill_file.read_text()
        missing = [section for section in REQUIRED_SECTIONS if section not in content]
        if missing:
            missing_by_file[str(skill_file.relative_to(root))] = missing

    for skill_path, missing in missing_by_file.items():
        print(f"[canonical-sections] {skill_path} missing: {', '.join(missing)}")
    return 1 if missing_by_file else 0


def validate_cross_references(root: Path) -> int:
    """Validate that skill-to-skill references point to existing skill files.

    Flags a reference when a "`<name>` skill" handoff idiom or a
    ``skills/<name>.md`` markdown link names a file that does not exist.

    Args:
        root: Repository root path.

    Returns:
        Zero when every cross-skill reference resolves.
    """
    skills_dir = root / "skills"
    valid = {path.stem for path in skills_dir.glob("*.md")}

    broken_by_file: dict[str, list[str]] = {}
    for skill_file in sorted(skills_dir.glob("*.md")):
        content = skill_file.read_text()
        referenced = {match.group(1) for match in _SKILL_REF.finditer(content)}
        referenced |= {match.group(2) for match in _SKILL_LINK.finditer(content)}
        broken = sorted(name for name in referenced if name not in valid)
        if broken:
            broken_by_file[str(skill_file.relative_to(root))] = broken

    for skill_path, broken in broken_by_file.items():
        print(f"[cross-reference] {skill_path} references missing skill(s): {', '.join(broken)}")
    return 1 if broken_by_file else 0


def validate_line_budget(root: Path) -> int:
    """Validate every skill file stays within MAX_SKILL_LINES lines.

    Args:
        root: Repository root path.

    Returns:
        Zero when no skill file exceeds the line budget.
    """
    over_budget: dict[str, int] = {}
    for skill_file in sorted((root / "skills").glob("*.md")):
        count = len(skill_file.read_text().splitlines())
        if count > MAX_SKILL_LINES:
            over_budget[str(skill_file.relative_to(root))] = count

    for skill_path, count in over_budget.items():
        print(f"[line-budget] {skill_path} has {count} lines (max {MAX_SKILL_LINES})")
    return 1 if over_budget else 0


def frontmatter_problems(stem: str, fields: dict[str, str] | None) -> list[str]:
    """List every way one skill's frontmatter breaks the authoring rules.

    Args:
        stem: Skill file name without extension; ``name`` must equal it.
        fields: Parsed frontmatter, or None when the block is missing.

    Returns:
        Human-readable problems; empty when the frontmatter is valid.
    """
    if fields is None:
        return ["missing --- frontmatter block"]

    problems: list[str] = []
    name = fields.get("name", "")
    if name != stem:
        problems.append(f"name {name!r} must equal file stem {stem!r}")
    if not _SKILL_NAME.fullmatch(name) or len(name) > MAX_NAME_CHARS:
        problems.append(f"name must be lowercase/digits/hyphens, max {MAX_NAME_CHARS} chars")
    if any(word in name for word in RESERVED_NAME_WORDS):
        problems.append(f"name must not contain {' or '.join(RESERVED_NAME_WORDS)}")

    description = fields.get("description", "")
    if not description:
        problems.append("description is empty")
    if len(description) > MAX_DESCRIPTION_CHARS:
        problems.append(f"description has {len(description)} chars (max {MAX_DESCRIPTION_CHARS})")
    if "<" in description or ">" in description:
        problems.append("description must not contain XML tags or angle brackets")
    if PLACEHOLDER_DESCRIPTION in description:
        problems.append("description is the generic placeholder")
    if description and TRIGGER_PHRASE not in description:
        problems.append(f"description must say when to use the skill ({TRIGGER_PHRASE!r} ...)")
    return problems


def validate_frontmatter(root: Path) -> int:
    """Validate every skill's name and description frontmatter.

    Args:
        root: Repository root path.

    Returns:
        Zero when every skill file has valid frontmatter.
    """
    problems_by_file: dict[str, list[str]] = {}
    for skill_file in sorted((root / "skills").glob("*.md")):
        fields = parse_frontmatter(skill_file.read_text())
        problems = frontmatter_problems(skill_file.stem, fields)
        if problems:
            problems_by_file[str(skill_file.relative_to(root))] = problems

    for skill_path, problems in problems_by_file.items():
        print(f"[frontmatter] {skill_path}: {'; '.join(problems)}")
    return 1 if problems_by_file else 0


def run(cmd: list[str], cwd: Path) -> int:
    """Run one command in the repository root.

    Args:
        cmd: Command and args to execute.
        cwd: Working directory for the command.

    Returns:
        Process exit code.
    """
    proc = subprocess.run(cmd, cwd=cwd, check=False)
    return proc.returncode


def main() -> int:
    """Run lint, YAML validation, and skill structural checks.

    Runs ``make lint`` and ``make validate``, then the skill-compliance,
    canonical-section, cross-reference, line-budget, and frontmatter checks
    over ``skills/*.md``.

    Returns:
        Zero when all checks pass, non-zero otherwise.
    """
    root = Path(__file__).resolve().parents[5]

    # Guard against silently passing when the skills directory is missing or
    # empty: an empty glob would make every per-skill check vacuously succeed.
    skills = list((root / "skills").glob("*.md"))
    if not skills:
        print(f"[audit] no skill files found under {root / 'skills'} — refusing to pass vacuously")
        return 1

    commands = [["make", "lint"], ["make", "validate"]]
    for cmd in commands:
        code = run(cmd, root)
        if code != 0:
            return code

    checks = (
        validate_skill_compliance,
        validate_canonical_sections,
        validate_cross_references,
        validate_line_budget,
        validate_frontmatter,
    )
    # Run every check (do not short-circuit) so all failures are reported at once.
    results = [check(root) for check in checks]
    return 1 if any(code != 0 for code in results) else 0


if __name__ == "__main__":
    sys.exit(main())
