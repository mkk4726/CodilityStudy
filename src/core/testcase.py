"""Load `.txt` test-case files and validate a solution function against them.

Test-case file format: one JSON object per line.
    {"input": {"arr1": [[1, 4], [3, 2]], "arr2": [[3, 3], [3, 3]]}, "expected": [[15, 15], [15, 15]]}

`input` is passed to the solution function as keyword arguments, so its keys
must match the function's parameter names. Blank lines and lines starting
with `#` are ignored.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

Comparator = Callable[[Any, Any], bool]


@dataclass
class TestCase:
    name: str
    input: dict[str, Any]
    expected: Any


@dataclass
class TestResult:
    case: TestCase
    actual: Any
    passed: bool


def load_testcases(path: str | Path) -> list[TestCase]:
    path = Path(path)
    cases = []
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"{path}:{lineno}: invalid JSON test case - {e}") from e
        cases.append(TestCase(name=data.get("name", f"{path.stem}[{lineno}]"), input=data["input"], expected=data["expected"]))
    return cases


def run_testcases(func: Callable[..., Any], testcases: list[TestCase], compare: Comparator | None = None) -> list[TestResult]:
    compare = compare or (lambda actual, expected: actual == expected)
    results = []
    for case in testcases:
        actual = func(**case.input)
        results.append(TestResult(case=case, actual=actual, passed=compare(actual, case.expected)))
    return results


def assert_testcases(func: Callable[..., Any], path: str | Path, compare: Comparator | None = None) -> None:
    results = run_testcases(func, load_testcases(path), compare=compare)
    failures = [r for r in results if not r.passed]
    if failures:
        detail = "\n".join(f"  - {r.case.name}: input={r.case.input} expected={r.case.expected} actual={r.actual}" for r in failures)
        raise AssertionError(f"{len(failures)}/{len(results)} test case(s) failed:\n{detail}")
