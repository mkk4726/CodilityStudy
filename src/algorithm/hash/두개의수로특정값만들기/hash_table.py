from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(arr: list[int], target: int) -> bool:
    hash = [0] * (target + 1)

    for num in arr:
        if num <= target:
            hash[num] = 1

    for num in arr:
        if (num >= target):
            continue
            
        if ((target - num) == num):
            continue
            
        if (hash[target - num]):
            return True

    return False


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
