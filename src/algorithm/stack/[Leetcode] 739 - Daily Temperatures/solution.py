from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)

    for i, temperature in enumerate(temperatures):
        while len(stack) > 0 and temperatures[stack[-1]] < temperature:
            k = stack.pop()
            answer[k] = i - k
        stack.append(i)
        
    return answer


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
