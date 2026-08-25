from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(record):
    record_hash = {}

    for rec in record:
        rec_list = rec.split(" ")
        action, uid = rec_list[0], rec_list[1]
        
        if action in ["Enter", "Change"]:
            record_hash[uid] = rec_list[2]
            
    expected = []

    for rec in record:
        rec_list = rec.split(" ")
        action, uid = rec_list[0], rec_list[1]
        if action == "Change":
            continue
        
        action_str = "들어왔습니다." if action == "Enter" else "나갔습니다."
        
        expected.append(f"{record_hash[uid]}님이 {action_str}")
    
    return expected


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
