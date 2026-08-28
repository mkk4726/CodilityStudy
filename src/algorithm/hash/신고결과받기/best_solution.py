"""https://school.programmers.co.kr/learn/courses/30/lessons/92334

피드백
- 핵심은 동일 (신고자, 대상)을 1회로 치는 것이다. example2가 깨진 이유가 여기다.
  report_hash는 set이라 중복을 막았는데 reported_cnt는 매번 +1 해서 con이 4회로 집계됐다.
  신고자 집합을 두고 len(집합)이 곧 신고 횟수면 카운터를 따로 둘 필요가 없다.
- report_hash(내가 신고한 사람)와 reported_hash(나를 신고한 사람)는 서로 역방향이다.
  대상 -> 신고자 집합 하나만 있으면 정지 여부와 메일 대상을 모두 만들 수 있다.
- if key not in dict else는 defaultdict(set)이면 add만 하면 된다.
- a, b보다 reporter, target이 역할이 분명하다. id는 내장 함수 이름이라 uid가 낫다.
"""

from collections import defaultdict
from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(id_list: list[str], report: list[str], k: int) -> list[int]:
    reported_by: dict[str, set[str]] = defaultdict(set)

    for rec in report:
        reporter, target = rec.split()
        reported_by[target].add(reporter)

    mail = {uid: 0 for uid in id_list}
    for reporters in reported_by.values():
        if len(reporters) >= k:
            for reporter in reporters:
                mail[reporter] += 1

    return [mail[uid] for uid in id_list]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
