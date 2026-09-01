"""피드백
- 순회 정의(전위/중위/후위)는 맞다. 방문 시점만 바꿔서 세 함수를 만든 것도 맞다.
- visited + 부모로 되돌아가기는 재귀를 직접 구현한 것과 같다. 동작은 맞지만
  호출 스택이 그 일을 대신하므로 while/visited/부모 인덱스는 필요 없다.
- 더미 [0] + 1-based는 힙 공식(왼쪽 2i, 오른쪽 2i+1)을 쓰기 위함이다.
  0-based면 왼쪽 2i+1, 오른쪽 2i+2로 원본 배열을 그대로 쓴다.
- 트리는 이미 배열이라 Pointer로 다시 만들 필요가 없다.
- 세 순회는 재귀 한 함수에서 현재 노드를 붙이는 위치만 바꾸면 된다.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(nodes: list[int]) -> list[str]:
    def dfs(idx: int, order: str) -> str:
        if idx >= len(nodes):
            return ""

        left = dfs(idx * 2 + 1, order)
        right = dfs(idx * 2 + 2, order)
        cur = str(nodes[idx])

        if order == "pre":
            return cur + left + right
        if order == "in":
            return left + cur + right
        return left + right + cur

    return [dfs(0, "pre"), dfs(0, "in"), dfs(0, "post")]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
