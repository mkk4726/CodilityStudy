"""https://school.programmers.co.kr/learn/courses/30/lessons/42579

피드백
- 장르 총합으로 순서를 정한 뒤 장르 안에서 곡을 고르는 2단 정렬이 맞다.
  해시 두 개로 역할을 나누면 된다. 총재생은 장르 순서, (고유번호, 재생수) 목록은 장르 안 곡 선택.
- 곡 정렬 키 (-play, index)가 규칙을 그대로 담는다. 재생 수 내림차순, 동점이면 고유 번호 오름차순.
- sorted(sum_by_genre, reverse=True)는 장르 이름을 사전 역순으로 정렬한다.
  example1은 pop > classic이라 우연히 통과하고, 총재생 순이 이름 순과 다르면 깨진다.
  key=lambda g: total_by_genre[g]가 맞다.
- if genre in ... else는 defaultdict면 한 줄이다.
- if i >= 2: continue는 나머지 곡을 계속 돈다. songs[:2]가 의도에 맞다.
- genre_numbers의 원소는 번호가 아니라 (고유번호, 재생수)다. songs_by_genre가 더 분명하다.
"""

from collections import defaultdict
from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(genres: list[str], plays: list[int]) -> list[int]:
    total_by_genre: dict[str, int] = defaultdict(int)
    songs_by_genre: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_by_genre[genre] += play
        songs_by_genre[genre].append((i, play))

    result = []
    for genre in sorted(total_by_genre, key=lambda g: total_by_genre[g], reverse=True):
        songs = sorted(songs_by_genre[genre], key=lambda song: (-song[1], song[0]))
        result.extend(i for i, _ in songs[:2])
    return result


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
