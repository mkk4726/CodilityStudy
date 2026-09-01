from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(nodes: list[int]) -> list[str]:
    def preorder(idx: int) -> str:
        if idx >= len(nodes):
            return ""
        return str(nodes[idx]) + preorder(idx * 2 + 1) + preorder(idx * 2 + 2)

    def inorder(idx: int) -> str:
        if idx >= len(nodes):
            return ""
        return inorder(idx * 2 + 1) + str(nodes[idx]) + inorder(idx * 2 + 2)

    def postorder(idx: int) -> str:
        if idx >= len(nodes):
            return ""
        return postorder(idx * 2 + 1) + postorder(idx * 2 + 2) + str(nodes[idx])

    return [preorder(0), inorder(0), postorder(0)]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
