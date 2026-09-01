from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def pre_search(node_list: list[int]) -> list[int]:
    current_node = 1
    result = []
    visited = [False] * len(node_list)

    while True:
        if not visited[current_node]:
            result.append(node_list[current_node])
            visited[current_node] = True
        elif current_node * 2 < len(node_list) and not visited[current_node * 2]:
            current_node = current_node * 2
        elif current_node * 2 + 1 < len(node_list) and not visited[current_node * 2 + 1]:
            current_node = current_node * 2 + 1
        elif current_node // 2 > 0:
            current_node = current_node // 2
        else:
            break

    return result


def mid_search(node_list: list[int]) -> list[int]:
    current_node = 1
    result = []
    visited = [False] * len(node_list)

    while True:
        if current_node * 2 < len(node_list) and not visited[current_node * 2]:
            current_node = current_node * 2
        elif not visited[current_node]:
            result.append(node_list[current_node])
            visited[current_node] = True
        elif current_node * 2 + 1 < len(node_list) and not visited[current_node * 2 + 1]:
            current_node = current_node * 2 + 1
        elif current_node // 2 > 0:
            current_node = current_node // 2
        else:
            break

    return result


def post_search(node_list: list[int]) -> list[int]:
    current_node = 1
    result = []
    visited = [False] * len(node_list)

    while True:
        if current_node * 2 < len(node_list) and not visited[current_node * 2]:
            current_node = current_node * 2
        elif current_node * 2 + 1 < len(node_list) and not visited[current_node * 2 + 1]:
            current_node = current_node * 2 + 1
        elif not visited[current_node]:
            result.append(node_list[current_node])
            visited[current_node] = True
        elif current_node // 2 > 0:
            current_node = current_node // 2
        else:
            break

    return result


def solution(nodes: list[int]) -> list[str]:
    node_list = [0] + nodes
    return [
        "".join(str(x) for x in pre_search(node_list)),
        "".join(str(x) for x in mid_search(node_list)),
        "".join(str(x) for x in post_search(node_list)),
    ]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
