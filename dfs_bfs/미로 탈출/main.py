# 내 풀이

import argparse


def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


parser = argparse.ArgumentParser(description="Parse arguments with '--~' prefix.", prefix_chars="-~")

parser.add_argument("--file", type=str)

args = parser.parse_args()

# N X M 크기의 얼음틀
# 구멍 : 0, 칸막이 : 1
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주.

lines = read_txt_lines(f"/Users/visuworks/Desktop/CodilityStudy/dfs_bfs/미로 탈출/{args.__dict__.get('file')}.txt")

N, M = map(int, lines[0].split())
print(N, M)

miro = []
for line in lines[1:]:
    miro.append(list(map(int, line.strip())))

print(miro)


distances = []


def dfs(x, y, distance):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if miro[x][y] == 0:
        return False

    if x == N - 1 and y == M - 1:
        distances.append(distance)

    miro[x][y] = 0

    dfs(x - 1, y, distance + 1)
    dfs(x + 1, y, distance + 1)
    dfs(x, y - 1, distance + 1)
    dfs(x, y + 1, distance + 1)


dfs(0, 0, 1)

print(distances)
