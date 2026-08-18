from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(cards1: list[str], cards2: list[str], goal: list[str]) -> str:
    while goal:
        target_word = goal.pop(0)

        if cards1 and cards1[0] == target_word:
            cards1.pop(0)
        elif cards2 and cards2[0] == target_word:
            cards2.pop(0)
        else:
            return "No"
        
    return "Yes"


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
