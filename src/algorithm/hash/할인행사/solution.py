from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(want: list[str], number: list[int], discount: list[str]) -> int:
    want_number = {}
    for goods, cnt in zip(want, number):
        want_number[goods] = cnt
        
    count_hash = {key: 0 for key in want_number.keys()}
    
    first_window = discount[:10]

    for goods in first_window:
        if goods in count_hash: 
            count_hash[goods] += 1
        
    result = 1 if count_hash == want_number else 0
    
    for i in range(1, len(discount) - 9):
        if discount[i-1] in count_hash:
            count_hash[discount[i-1]] = max(0, count_hash[discount[i-1]] - 1)
        
        if discount[i+9] in count_hash:
            count_hash[discount[i+9]] = count_hash[discount[i+9]] + 1
        
        if count_hash == want_number:
            result += 1 
            
    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
