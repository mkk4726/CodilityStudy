from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(arr: list[int], target: int) -> bool:
    set_arr = set(arr)
    
    for value in arr:
        left = target - value
        if left <= 0 or value == left:
            continue
        if left in set_arr:
            return True
    
    return False


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
