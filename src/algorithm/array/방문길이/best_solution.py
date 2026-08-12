"""https://school.programmers.co.kr/learn/courses/30/lessons/49994"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"

MOVES = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
BOUND = 5


def solution(dirs: str) -> int:
    x, y = 0, 0
    visited: set[tuple[int, int, int, int]] = set()

    for d in dirs:
        dx, dy = MOVES[d]
        nx, ny = x + dx, y + dy

        # 경계를 넘는 명령은 무시한다.
        if not (-BOUND <= nx <= BOUND and -BOUND <= ny <= BOUND):
            continue

        # 방향에 상관없이 같은 구간이면 하나로 취급하도록 좌표쌍을 정렬해 저장한다.
        edge = (x, y, nx, ny) if (x, y) < (nx, ny) else (nx, ny, x, y)
        visited.add(edge)

        x, y = nx, ny

    return len(visited)


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
