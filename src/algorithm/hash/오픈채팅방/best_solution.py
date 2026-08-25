"""https://school.programmers.co.kr/learn/courses/30/lessons/42888

피드백
- 메시지는 이벤트 시점의 닉이 아니라 최종 닉으로 다시 그려야 한다.
  그래서 uid -> 최종 닉을 먼저 모은 뒤 Enter/Leave만 출력하는 두 단계가 맞다.
  Change는 메시지를 남기지 않고 닉만 갱신한다. 닉은 중복될 수 있으므로 키는 uid다.
- 같은 문자열을 두 번 split할 필요는 없다. 한 번 나눠서 닉 갱신과 (action, uid) 기록을 같이 한다.
- split(" ")보다 split()이 공백 처리에 더 안전하다.
- expected는 테스트 기대값 이름이다. 반환 리스트는 result가 맞다.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"

MESSAGES = {
    "Enter": "들어왔습니다.",
    "Leave": "나갔습니다.",
}


def solution(record: list[str]) -> list[str]:
    nick: dict[str, str] = {}
    events: list[tuple[str, str]] = []

    for rec in record:
        action, uid, *rest = rec.split()
        if action in ("Enter", "Change"):
            nick[uid] = rest[0]
        if action != "Change":
            events.append((action, uid))

    return [f"{nick[uid]}님이 {MESSAGES[action]}" for action, uid in events]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
