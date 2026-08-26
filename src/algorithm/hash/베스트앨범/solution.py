from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(genres: list[str], plays: list[int]) -> list[int]:
    sum_by_genre = {}
    genre_numbers = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in sum_by_genre:
            sum_by_genre[genre] += play
        else:
            sum_by_genre[genre] = play
            
        if genre in genre_numbers:
            genre_numbers[genre].append((i, play))
        else:
            genre_numbers[genre] = [(i, play)]
            
    genre_list = sorted(sum_by_genre, key=lambda x: sum_by_genre[x], reverse=True)    
    
    result = []

    for genre in genre_list:
        numbers = genre_numbers[genre]
        numbers = sorted(numbers, key=lambda x: (-x[-1], x[0]))
        for i, number in enumerate(numbers):
            if i >= 2:
                continue
            result.append(number[0])
            
    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
