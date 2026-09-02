"""피드백
- BST 규칙(작으면 왼쪽, 크면 오른쪽)과 삽입/탐색 분리는 맞다. 테스트도 통과한다.
- Tree는 이미 있는 Pointer와 같다. value/data 이름만 다르다. left/right 기본값을
  None으로 두면 Tree(value)만 쓰면 된다.
- 삽입의 while True + 빈 칸이면 break는 재귀를 손으로 펼친 것이다.
  “여기가 비었으면 만들고, 아니면 왼쪽 또는 오른쪽으로 같은 일을 한다”가
  한 노드 계약이다. 탐색은 이미 그 형태라 재귀로 옮기기 쉽다.
- current_tree는 트리 전체가 아니라 지금 보고 있는 노드라 node가 더 맞다.
- lst에 중복이 없으므로 삽입에서 == 분기는 필요 없다. 같은 값이 오면
  지금 코드는 왼쪽으로 간다.
"""

from pathlib import Path

from src.algorithm.tree.pointer import Pointer
from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def insert(node: Pointer | None, value: int) -> Pointer:
    if node is None:
        return Pointer(value)
    if value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def search(node: Pointer | None, value: int) -> bool:
    if node is None:
        return False
    if node.data == value:
        return True
    if value < node.data:
        return search(node.left, value)
    return search(node.right, value)


def solution(lst: list[int], search_lst: list[int]) -> list[bool]:
    root: Pointer | None = None
    for value in lst:
        root = insert(root, value)
    return [search(root, value) for value in search_lst]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
