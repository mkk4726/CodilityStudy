from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(s: str) -> bool:
    # 스택에 쌓다가 top이랑 같으면 짝이니까 pop, 다르면 push
    # 다 끝나고 스택이 비어있으면 성공

    # def delete_dups(s:str) -> str | bool:
    #     for i in range(len(s)-1):
    #         if s[i] == s[i+1]:
    #             return s[:i] + s[i+2:]
        
    #     return False

    # while s:
    #     s = delete_dups(s)

    # # 10^6 이 문제 조건이라서 O(N^2) 은 시간초과되는군? 처음 풀이

    # 

    stack = []

    for alphabet in s:
        if len(stack) > 0:
            before_alphabet = stack.pop()
            if before_alphabet == alphabet:
                continue
            else:
                stack.append(before_alphabet)
                stack.append(alphabet)
        else:
            stack.append(alphabet)

    return int(len(stack)==0)


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
