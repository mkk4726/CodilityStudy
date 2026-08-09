"""https://school.programmers.co.kr/learn/courses/30/lessons/12949"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    m, n = len(arr1), len(arr2[0])

    result = [[-1 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            tmp = 0
            # 행이랑 열을 곱하기
            for k in range(len(arr2)):
                tmp += arr1[i][k] * arr2[k][j]
            result[i][j] = tmp

    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
