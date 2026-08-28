from collections import Counter
from itertools import combinations
from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(orders: list[str], course: list[int]) -> list[str]:
    counter = Counter()

    for order in orders:
        sorted_order = sorted(order)
        for size in course:
            for combo in combinations(sorted_order, size):
                counter[''.join(combo)] += 1

    answer = []
    for size in course:
        candidates = {combo: cnt for combo, cnt in counter.items() if len(combo) == size}
        if not candidates:
            continue

        max_count = max(candidates.values())
        if max_count >= 2:
            answer.extend(combo for combo, cnt in candidates.items() if cnt == max_count)

    return sorted(answer)


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
