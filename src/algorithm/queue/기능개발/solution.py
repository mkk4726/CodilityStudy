from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    days = []

    for progress, speed, in zip(progresses, speeds):
        left_progress = 100 - progress
        day = left_progress / speed
        day = int(day) if int(day) == day else int(day) + 1
        days.append(day)

    result = []

    f_day = days.pop(0)
    cnt = 1
        
    while days:
        if days[0] <= f_day:
            cnt += 1
            days.pop(0)
        else:
            result.append(cnt)
            f_day = days.pop(0)
            cnt = 1

    result.append(cnt)

    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
