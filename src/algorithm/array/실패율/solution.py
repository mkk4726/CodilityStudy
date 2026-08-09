"""https://school.programmers.co.kr/learn/courses/30/lessons/42889"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(N: int, stages: list[int]) -> list[int]:

    fail_rate = []

    for i in range(1, N + 1):
        on_going_cnt = 0  # i == stage
        after_all_cnt = 0  # i >= stage

        for stage in stages:
            if stage == i:
                on_going_cnt += 1
            if stage >= i:
                after_all_cnt += 1

        rate = on_going_cnt / after_all_cnt if after_all_cnt > 0 else 0
        fail_rate.append([i, rate])

    # reverse=True와 함께 sort()가 stable하므로 동률인 스테이지는 원래 순서(오름차순)를 유지한다.
    return [x[0] for x in sorted(fail_rate, key=lambda x: x[1], reverse=True)]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()