"""https://school.programmers.co.kr/learn/courses/30/lessons/49994"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(dirs: str) -> int:
    state = (0, 0)

    movement_dict = {"U": (0, +1), "D": (0, -1), "L": (-1, 0), "R": (+1, 0)}

    loads = []

    for dir in dirs:
        movement = movement_dict[dir]
        dx, dy = movement
        x, y = state
        
        new_x = x + dx
        new_y = y + dy
        
        new_x = min(max(-5, new_x), 5)
        new_y = min(max(-5, new_y), 5)

        if (x != new_x or y != new_y) and (x, y, new_x, new_y) not in loads and (new_x, new_y, x, y) not in loads:
            loads.append((x, y, new_x, new_y))

        state = (new_x, new_y)

    return len(loads)


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
