"""https://school.programmers.co.kr/learn/courses/30/lessons/42586

피드백
- days.pop(0)로 큐처럼 앞을 계속 빼면 매번 리스트가 당겨져 사실상 O(n^2)이 된다.
  인덱스로 한 번만 순회하면서 최댓값만 갱신하면 O(n)으로 끝난다.
- 수동으로 올림 처리(int(day) 비교)하는 대신 math.ceil을 쓰면 의도가 바로 드러난다.
- 그룹의 기준이 되는 "현재까지의 최대 배포일"이라는 의미를 이름에 담아야
  (f_day 대신 current_deploy_day) 코드만 보고도 역할이 파악된다.
"""

import math
from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    days = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]

    result = []
    current_deploy_day = days[0]
    count = 0

    for day in days:
        if day > current_deploy_day:
            result.append(count)
            current_deploy_day = day
            count = 0
        count += 1

    result.append(count)

    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
