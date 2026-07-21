"""Run repository audit checks.

This helper re-runs baseline repository checks used in the audit workflow.
It executes the existing Makefile validation commands and returns a non-zero
status code if any command fails.
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
    root = Path(__file__).resolve().parents[1]
    commands = [["make", "lint"], ["make", "validate"]]
    for cmd in commands:
        code = run(cmd, root)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    sys.exit(main())
