from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(prices: list[int]) -> list[int]:
    stack = []
    len_prices = len(prices)

    result = [0] * len_prices

    for i, price in enumerate(prices):
        while len(stack) > 0 and stack[-1][1] > price:
            past_i, past_price = stack[-1]
            result[past_i] = i - past_i
            stack.pop()
        stack.append((i, price))

    while stack:
        top = stack.pop()
        i, price = top
        result[i] = len_prices - i - 1

    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
