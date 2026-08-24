"""https://school.programmers.co.kr/learn/courses/30/lessons/131127

피드백
- 슬라이딩 윈도우 접근 자체가 정확하다. 매 윈도우를 새로 세지 않고
  왼쪽에서 빠지는 값 -1 / 오른쪽에서 들어오는 값 +1로 갱신해서 O(n)에 푼다.
- count_hash는 want에 있는 상품만 키로 들고 있고, number의 합이 항상 10이라는
  제약(윈도우 크기와 동일) 덕분에 count_hash == want_number 비교만으로
  "원하는 수량대로 10일 연속 일치하는지"를 정확히 판별할 수 있다.
- max(0, count_hash[...] - 1)은 불필요한 방어 코드였다. 왼쪽에서 빠지는 상품은
  반드시 직전 윈도우에 포함돼 있었으므로 카운트가 음수가 될 수 없다.
  없어도 되는 방어 코드는 "혹시 버그가 있나"라는 의문만 남기므로 제거한다.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(want: list[str], number: list[int], discount: list[str]) -> int:
    want_number = dict(zip(want, number))
    count_hash = {goods: 0 for goods in want_number}

    for goods in discount[:10]:
        if goods in count_hash:
            count_hash[goods] += 1

    result = 1 if count_hash == want_number else 0

    for i in range(1, len(discount) - 9):
        left, right = discount[i - 1], discount[i + 9]

        if left in count_hash:
            count_hash[left] -= 1
        if right in count_hash:
            count_hash[right] += 1

        if count_hash == want_number:
            result += 1

    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
