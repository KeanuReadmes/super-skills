"""Audit command-line entrypoint.

This module runs baseline repository quality checks used by the audit process.
It is designed to run inside the tools uv workspace as a Python monorepo app.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


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
    """Run lint and YAML validation checks.

    Returns:
        Zero when all checks pass, non-zero otherwise.
    """
    root = Path(__file__).resolve().parents[5]
    commands = [["make", "lint"], ["make", "validate"]]
    for cmd in commands:
        code = run(cmd, root)
        if code != 0:
            return code
    if validate_skill_compliance(root) != 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
