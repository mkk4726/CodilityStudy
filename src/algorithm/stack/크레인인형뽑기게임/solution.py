from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(board: list[list[int]], moves: list[int]) -> int:
    board_stacks = [[]]

    for i in range(len(board)):
        board_stacks.append([row[i] for row in board if row[i] > 0][::-1]) 

    result_stack = []
    delete_cnt = 0

    for move in moves:
        if len(board_stacks[move]) == 0:
            continue

        top = board_stacks[move].pop()
        if len(result_stack) > 0 and result_stack[-1] == top:
            result_stack.pop()
            delete_cnt += 2
        else:
            result_stack.append(top)

    return delete_cnt


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
