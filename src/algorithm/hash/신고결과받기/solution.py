from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(id_list: list[str], report: list[str], k: int) -> list[int]:
    # 유저별로 본인이 신고한 대상

    report_hash = {}
    reported_hash = {}
    reported_cnt = {}

    for declaration in report:
        a, b = declaration.split()
        if a not in report_hash:
            report_hash[a] = {b}
        else:
            report_hash[a].add(b)
        
        if b not in reported_hash: 
            reported_hash[b] = {a}
            reported_cnt[b] = 1
        else: # 중복제거 로직이 필요함
            if a not in reported_hash[b]:
                reported_hash[b].add(a)
                reported_cnt[b] += 1
            
    result = []

    for id in id_list:
        tmp_cnt = 0

        # 본인이 신고한 대상 뽑기
        if id in report_hash:
            report_list = report_hash[id]
            for user in report_list:
                if reported_cnt[user] >= k:
                    tmp_cnt += 1

        result.append(tmp_cnt)
    
    return result



def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
