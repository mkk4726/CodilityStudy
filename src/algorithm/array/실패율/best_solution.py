"""https://school.programmers.co.kr/learn/courses/30/lessons/42889"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(n: int, stages: list[int]) -> list[int]:
    # stages를 한 번만 순회해서 스테이지별 정지 인원을 센다. O(M)
    stuck_cnt = [0] * (n + 2)
    for stage in stages:
        stuck_cnt[stage] += 1

    fail_rate = []
    reached_cnt = len(stages)  # 아직 클리어하지 못하고 남아있는(=이 스테이지에 도달한) 인원

    for i in range(1, n + 1):
        # 매 스테이지마다 stages를 다시 스캔하지 않고, reached_cnt를 누적 차감한다. O(N)
        rate = stuck_cnt[i] / reached_cnt if reached_cnt > 0 else 0
        fail_rate.append((i, rate))
        reached_cnt -= stuck_cnt[i]

    # 동점일 때 스테이지 번호가 작은 쪽이 먼저 오도록 2차 키를 명시한다.
    fail_rate.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, _ in fail_rate]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
