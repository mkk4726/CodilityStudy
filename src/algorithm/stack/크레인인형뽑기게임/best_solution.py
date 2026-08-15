"""https://school.programmers.co.kr/learn/courses/30/lessons/64061

피드백
- 열을 스택으로 만들고 바구니는 짝지어 제거하기와 같은 스택으로 처리한 구성이 정석이다.
- board_stacks[0]을 비워 두고 moves의 1-based 열 번호를 그대로 인덱스로 쓰는 점이 깔끔하다.
- 열을 미리 쌓아 pop으로 집으면 매 move마다 0을 훑지 않아도 된다. N<=30이라 안 해도 통과하지만 스택 모델링이 맞다.
- 전처리 O(N^2), 크레인 O(M). 제한이 작아서 더 줄일 필요는 없다.
- 반환값은 폭발 횟수가 아니라 사라진 인형 수이므로 한 번에 += 2.
- board의 원소는 행이다. for column in board가 아니라 for row in board로 두고, 열 i는 row[i]로 뽑는다.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(board: list[list[int]], moves: list[int]) -> int:
    # 인덱스 0은 더미. moves가 1-based이므로 열 번호를 그대로 쓴다.
    # board는 행의 리스트이므로, 열 i는 각 row[i]를 모아 만든다. 0을 빼고 뒤집어 맨 위가 pop 되게 한다.
    columns: list[list[int]] = [[]]
    for i in range(len(board)):
        columns.append([row[i] for row in board if row[i] > 0][::-1])

    basket: list[int] = []
    removed = 0

    for move in moves:
        if not columns[move]:
            continue

        doll = columns[move].pop()
        if basket and basket[-1] == doll:
            basket.pop()
            removed += 2
        else:
            basket.append(doll)

    return removed


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
