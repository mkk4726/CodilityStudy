from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(n: int, k: int) -> int:
    from collections import deque

    dq = deque(range(1, n+1))
    while len(dq) != 1:
        # 앞에서 K번째 뽑기
        # popleft(2) 이런건 없는거고
        # k만큼 뽑고 맨마지막 제외하고는 다시 넣어야하는데?
        for i in range(1, k+1):
            left = dq.popleft()
            if i != k:
                dq.append(left)

    return dq[0]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
