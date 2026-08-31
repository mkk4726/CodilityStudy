from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(prices: list[int]) -> list[int]:
    answer = prices.copy()
    stack: list[int] = []  # 아직 할인 짝을 못 찾은 인덱스들 (오름차순 유지)

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
            k = stack.pop()
            answer[k] -= price
        stack.append(i)

    return answer


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
