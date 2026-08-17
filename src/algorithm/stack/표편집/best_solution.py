"""https://school.programmers.co.kr/learn/courses/30/lessons/81303

피드백
- 행을 인덱스로 두고 prev/next 배열로 이중 연결 리스트를 만들면 U/D/C/Z가 모두 연결 연산으로 끝난다.
- 삭제된 행을 스택에 쌓아 Z는 LIFO 복구. 복구 시 커서(k)는 바꾸지 않는다.
- 인덱스 +1/-1로 삭제 행을 건너뛰면 n, cmd가 커서 시간 초과. 이웃만 따라가면 이동 합이 제한 안에 들어온다.
- set으로 삭제 여부만 O(1)로 봐도, 한 칸씩 걷는 구조면 효율성에서 막힌다.
- 마지막 결과는 스택에 남은 행만 X, 나머지는 O.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(n: int, k: int, cmd: list[str]) -> str:
    # 양끝은 이웃 없음을 -1로 표시
    prev = [i - 1 for i in range(n)]
    next_ = [i + 1 for i in range(n)]
    next_[-1] = -1

    stack: list[int] = []
    cur = k

    for command in cmd:
        op = command[0]

        if op == "U":
            x = int(command.split()[1])
            for _ in range(x):
                cur = prev[cur]
        elif op == "D":
            x = int(command.split()[1])
            for _ in range(x):
                cur = next_[cur]
        elif op == "C":
            stack.append(cur)
            up, down = prev[cur], next_[cur]

            # 양옆을 서로 이어 현재 행을 리스트에서 제거
            if up != -1:
                next_[up] = down
            if down != -1:
                prev[down] = up

            # 아래가 있으면 아래로, 없으면 위로
            cur = down if down != -1 else up
        else:  # Z
            row = stack.pop()
            up, down = prev[row], next_[row]

            # 삭제 직점에 기억해 둔 양옆 사이에 다시 끼워 넣기
            if up != -1:
                next_[up] = row
            if down != -1:
                prev[down] = row

    answer = ["O"] * n
    for row in stack:
        answer[row] = "X"
    return "".join(answer)


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
