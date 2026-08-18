"""https://school.programmers.co.kr/learn/courses/30/lessons/159994

피드백
- 두 뭉치의 맨 앞만 볼 수 있다는 제약을 greedy로 옮긴 전략은 맞다.
  단어가 두 뭉치에 겹치지 않으므로 앞이 일치하는 쪽만 쓰면 되고, 둘 다 아니면 "No"다.
- 리스트 pop(0)은 앞을 뺄 때마다 나머지가 당겨져 O(n)이다. goal/cards1/cards2에
  반복하면 이론상 O(n^2). 이 문제는 n<=10이라 통과하지만, 앞만 빼는 구조면 deque.popleft()가 맞다.
- 원본 리스트를 직접 pop하면 입력이 파괴된다. deque로 복사해 쓰면 원본은 그대로 둔다.
- print는 디버그 잔재이므로 최종본에서는 뺀다.
"""

from collections import deque
from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(cards1: list[str], cards2: list[str], goal: list[str]) -> str:
    q1 = deque(cards1)
    q2 = deque(cards2)

    for word in goal:
        if q1 and q1[0] == word:
            q1.popleft()
        elif q2 and q2[0] == word:
            q2.popleft()
        else:
            return "No"

    return "Yes"


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
