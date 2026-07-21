"""Audit command-line entrypoint.

This module runs baseline repository quality checks used by the audit process.
It is designed to run inside the tools uv workspace as a Python monorepo app.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


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
    return 0


if __name__ == "__main__":
    sys.exit(main())
