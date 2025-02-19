# 동빈나 풀이


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

lines = read_txt_lines(f"/Users/visuworks/Desktop/CodilityStudy/dfs_bfs/음료수 얼려 먹기/{args.__dict__.get('file')}.txt")

N, M = map(int, lines[0].split())
print(N, M)

ice_bucket = []
for line in lines[1:]:
    ice_bucket.append(list(map(int, line.strip())))

print(ice_bucket)


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if ice_bucket[x][y] == 0:
        ice_bucket[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) is True:
            result += 1

print(result)
