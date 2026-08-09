import pytest

from src.core import assert_testcases, load_testcases, run_testcases


@pytest.fixture
def sample_testcase_file(tmp_path):
    path = tmp_path / "cases.txt"
    path.write_text(
        '{"input": {"a": 1, "b": 2}, "expected": 3}\n'
        "\n"
        "# a comment line\n"
        '{"name": "negative", "input": {"a": -1, "b": -2}, "expected": -3}\n'
    )
    return path


def add(a, b):
    return a + b


def test_load_testcases_skips_blank_and_comment_lines(sample_testcase_file):
    cases = load_testcases(sample_testcase_file)
    assert [c.input for c in cases] == [{"a": 1, "b": 2}, {"a": -1, "b": -2}]
    assert cases[1].name == "negative"


def test_run_testcases_reports_pass_and_fail(sample_testcase_file):
    cases = load_testcases(sample_testcase_file)
    results = run_testcases(lambda a, b: a - b, cases)
    assert [r.passed for r in results] == [False, False]


def test_assert_testcases_passes_for_correct_solution(sample_testcase_file):
    assert_testcases(add, sample_testcase_file)


def test_assert_testcases_raises_for_incorrect_solution(sample_testcase_file):
    with pytest.raises(AssertionError, match="2/2 test case"):
        assert_testcases(lambda a, b: a * b, sample_testcase_file)
