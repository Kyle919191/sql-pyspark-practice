#!/usr/bin/env python3
"""Run a practice problem and compare output to expected.csv.

Usage:
    python tools/check.py sql/01-select/problems/01-organic-onsale
    python tools/check.py pyspark/01-select-filter/problems/01-organic-onsale
    python tools/check.py sql/01-select/problems/01-organic-onsale --solution
"""

from __future__ import annotations

import argparse
import json
import numbers
import runpy
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def _load_meta(problem_dir: Path) -> dict:
    meta_path = problem_dir / "meta.json"
    if not meta_path.exists():
        return {"ordered": False}
    return json.loads(meta_path.read_text())


def _cell(value):
    if value is None:
        return None
    try:
        if value is pd.NA or pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    if hasattr(value, "isoformat") and not isinstance(value, str):
        text = value.isoformat()
        return text[:10] if "T" in text or len(text) == 10 else text
    if isinstance(value, bool):
        return bool(value)
    if isinstance(value, numbers.Integral):
        return int(value)
    if isinstance(value, numbers.Real):
        number = float(value)
        if number.is_integer():
            return int(number)
        return round(number, 6)
    return str(value)


def _normalize(df: pd.DataFrame, ordered: bool) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c) for c in out.columns]
    for col in out.columns:
        out[col] = [_cell(v) for v in out[col].tolist()]
    if not ordered:
        out = out.sort_values(list(out.columns), kind="mergesort", na_position="last").reset_index(drop=True)
    else:
        out = out.reset_index(drop=True)
    return out




def _read_expected(problem_dir: Path) -> pd.DataFrame:
    return pd.read_csv(problem_dir / "expected.csv")


def _run_sql(problem_dir: Path, source_name: str) -> pd.DataFrame:
    import duckdb

    setup = (problem_dir / "setup.sql").read_text()
    query = (problem_dir / source_name).read_text().strip()
    if not query or query.startswith("-- write"):
        raise SystemExit(f"{source_name} is still empty. Write a SELECT, then check again.")

    con = duckdb.connect()
    con.execute(setup)
    return con.execute(query).fetchdf()


def _run_pyspark(problem_dir: Path, source_name: str) -> pd.DataFrame:
    script = problem_dir / source_name
    text = script.read_text()
    if "result =" not in text or text.strip().endswith("result = None"):
        raise SystemExit(f"{source_name} must assign a DataFrame to `result`.")

    ns = runpy.run_path(str(script), run_name="__practice__")
    result = ns.get("result")
    if result is None:
        raise SystemExit("Your script ran, but `result` was not set.")

    spark = ns.get("spark")
    pdf = result.toPandas()
    if spark is not None:
        spark.stop()
    return pdf


def _print_frame(title: str, df: pd.DataFrame) -> None:
    print(f"\n{title}")
    print(df.to_string(index=False) if not df.empty else "(no rows)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a SQL or PySpark practice problem.")
    parser.add_argument("problem", help="Path to a problem folder")
    parser.add_argument(
        "--solution",
        action="store_true",
        help="Run solution.sql / solution.py instead of starter.*",
    )
    args = parser.parse_args()

    problem_dir = Path(args.problem)
    if not problem_dir.is_absolute():
        problem_dir = (Path.cwd() / problem_dir).resolve()
    if not problem_dir.is_dir():
        raise SystemExit(f"Not a problem folder: {problem_dir}")

    meta = _load_meta(problem_dir)
    ordered = bool(meta.get("ordered", False))

    if (problem_dir / "setup.sql").exists():
        source = "solution.sql" if args.solution else "starter.sql"
        got = _run_sql(problem_dir, source)
    elif (problem_dir / "starter.py").exists() or (problem_dir / "solution.py").exists():
        source = "solution.py" if args.solution else "starter.py"
        sys.path.insert(0, str(ROOT))
        got = _run_pyspark(problem_dir, source)
    else:
        raise SystemExit(f"No starter.sql or starter.py in {problem_dir}")

    expected = _read_expected(problem_dir)
    if meta.get("result_columns"):
        cols = meta["result_columns"]
        missing = [c for c in cols if c not in got.columns]
        if missing:
            raise SystemExit(f"Your result is missing column(s): {missing}. Have: {list(got.columns)}")
        got = got[cols]
        expected = expected[cols]

    got_n = _normalize(got, ordered)
    exp_n = _normalize(expected, ordered)

    if got_n.equals(exp_n):
        print(f"PASS  {problem_dir.name}  ({len(got_n)} rows, source={source})")
        return 0

    print(f"FAIL  {problem_dir.name}  (source={source})")
    _print_frame("Your output", got)
    _print_frame("Expected", expected)
    print("\nTips: check column names, NULLs, and whether one row should exist per entity.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
