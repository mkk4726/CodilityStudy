from pathlib import Path
from pickle import TRUE

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(s: str) -> bool:
    # 감이 읎다
    # 열린 괄호가 있고 그 다음 그 수만큼 닫힌 괄호가 있으면 됨.
    # stack을 쓴다
    # 아 열린괄호는 stack에 넣고
    # 닫힌 괄호가 나오면 stack에서 꺼낼 수 있으면 true이고
    # 못꺼내면 false이구나?
    open_mark = []
    for mark in s:
        if mark == '(':
            open_mark.append(1)
        else:
            if len(open_mark) == 0:
                return False
            else:
                open_mark.pop()
    if len(open_mark) == 0:
        return True
    else:
        return False

def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
