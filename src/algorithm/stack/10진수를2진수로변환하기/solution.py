from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(n: int) -> str:
    # n이랑 가장 가까운 이진수를 어떻게 알지?
    # 가장 가까운 이진수부터 시작해서 위에서 아래로 빼면 될 것 같은디?
    # 


    raise NotImplementedError


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
