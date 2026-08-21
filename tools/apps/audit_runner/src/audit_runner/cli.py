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
    canonical-section, and cross-reference checks over ``skills/*.md``.

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
    )
    # Run every check (do not short-circuit) so all failures are reported at once.
    results = [check(root) for check in checks]
    return 1 if any(code != 0 for code in results) else 0


if __name__ == "__main__":
    sys.exit(main())
