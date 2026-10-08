#!/usr/bin/env python3
"""Check that the local practice stack can run."""

from __future__ import annotations

import shutil
import subprocess
import sys


def _ok(name: str, detail: str = "") -> None:
    suffix = f" — {detail}" if detail else ""
    print(f"  ok   {name}{suffix}")


def _fail(name: str, detail: str) -> None:
    print(f"  FAIL {name} — {detail}")


def main() -> int:
    failed = False
    print("Practice environment")

    if sys.version_info < (3, 10):
        _fail("python", f"{sys.version.split()[0]} (need 3.10+)")
        failed = True
    else:
        _ok("python", sys.version.split()[0])

    try:
        import duckdb

        _ok("duckdb", duckdb.__version__)
    except ImportError:
        _fail("duckdb", "run: pip install -r requirements.txt")
        failed = True

    try:
        import pandas

        _ok("pandas", pandas.__version__)
    except ImportError:
        _fail("pandas", "run: pip install -r requirements.txt")
        failed = True

    java = shutil.which("java")
    if java:
        try:
            proc = subprocess.run(
                ["java", "-version"],
                check=False,
                capture_output=True,
                text=True,
            )
            line = (proc.stderr or proc.stdout).splitlines()[0] if (proc.stderr or proc.stdout) else java
            major = None
            for token in line.replace('"', " ").split():
                if token[0].isdigit():
                    major = int(token.split(".")[0])
                    break
            if major is not None and major < 17:
                _fail("java", f"{line} (PySpark 4 needs 17+). Run: source tools/env.sh")
                failed = True
            else:
                _ok("java", line)
        except OSError as exc:
            _fail("java", str(exc))
            failed = True
    else:
        _fail("java", "needed for PySpark. Install a JDK 17, then source tools/env.sh")
        failed = True

    try:
        import pyspark

        _ok("pyspark", pyspark.__version__)
    except ImportError:
        _fail("pyspark", "run: pip install -r requirements.txt")
        failed = True

    if failed:
        print("\nFix the FAIL lines, then run this again.")
        return 1

    print("\nReady. Open STUDY_PLAN.md and start Day 1.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
