from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def polynomial_hash(s: str) -> int:
    p = 31
    m = 1_000_000_007
    hash_value = 0
    power = 1
    for char in s:
        hash_value = (hash_value + ord(char) * power) % m
        power = (power * p) % m
    return hash_value


def solution(string_list: list[str], query_list: list[str]) -> list[bool]:
    hashed = {polynomial_hash(s) for s in string_list}
    return [polynomial_hash(query) in hashed for query in query_list]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
