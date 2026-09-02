from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def search(search_number, base_tree):
    current_tree = base_tree

    while current_tree is not None:
        if current_tree.value == search_number:
            return True
        elif current_tree.value < search_number:
            current_tree = current_tree.right
        else:
            current_tree = current_tree.left

    return False


def solution(lst: list[int], search_lst: list[int]) -> list[bool]:
    base_tree = Tree(value=lst[0], left=None, right=None)

    for value in lst[1:]:
        current_tree = base_tree

        while True:
            if current_tree.value < value:
                if current_tree.right is None:
                    current_tree.right = Tree(value=value, left=None, right=None)
                    break
                else:
                    current_tree = current_tree.right
            else:
                if current_tree.left is None:
                    current_tree.left = Tree(value=value, left=None, right=None)
                    break
                else:
                    current_tree = current_tree.left

    return [search(search_number, base_tree) for search_number in search_lst]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
