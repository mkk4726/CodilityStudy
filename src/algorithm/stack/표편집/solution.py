from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(n: int, k: int, cmd: list[str]) -> str:
    deleted_index = []
    delete_things = set()

    curr_loc = k

    def move_down(curr_loc, d_down):
        while d_down > 0 and curr_loc < n-1:
            curr_loc += 1
            if curr_loc not in delete_things:
                d_down -= 1

        return curr_loc

    def move_up(curr_loc, d_up):
        while d_up > 0 and curr_loc > 0:
            curr_loc -= 1
            if curr_loc not in delete_things:
                d_up -= 1

        return curr_loc

    for command in cmd:
        if 'D' in command:
            curr_loc = move_down(curr_loc, int(command.split()[-1]))
        elif 'U' in command:
            curr_loc = move_up(curr_loc, int(command.split()[-1]))
        elif 'C' == command:
            deleted_index.append(curr_loc)
            delete_things.add(curr_loc)
            next_loc = move_down(curr_loc, 1)
            if curr_loc == next_loc:
                next_loc = move_up(curr_loc, 1)
            curr_loc = next_loc
        else: # Z 되돌리기
            index = deleted_index.pop()
            delete_things.remove(index)

    result_str = ""
    for i in range(n):
        if i in deleted_index:
            result_str += 'X'
        else:
            result_str += 'O'

    return result_str


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
