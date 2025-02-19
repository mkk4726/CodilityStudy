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

lines = read_txt_lines(f"/Users/visuworks/Desktop/CodilityStudy/dfs_bfs/음료수 얼려 먹기/{args.__dict__.get('file')}.txt")

N, M = map(int, lines[0].split())
print(N, M)

ice_bucket = []
for line in lines[1:]:
    ice_bucket.append(list(map(int, line.strip())))

print(ice_bucket)


# 특정 노드에서 이웃 노드 추출하는 코드
def get_neighbor(node, ice_bucket):
    x, y = node

    neighbors = []

    dx = [-1, 0, +1]
    dy = [-1, 0, +1]
    for i in range(len(dx)):
        for j in range(len(dy)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[j]

            if 0 <= tmp_x < len(ice_bucket) and 0 <= tmp_y < len(ice_bucket[0]):
                neighbors.append([tmp_x, tmp_y])

    return neighbors


# 0인 곳을 한 군데 잡아서 탐색 -> 탐색된 곳은 제외하고 나머지 0 중 하나를 선택해서 탐색 . 반복.
def dfs(node, ice_bucket, label):
    neighbors = get_neighbor(node, ice_bucket)

    for neighbor in neighbors:
        x, y = neighbor
        if ice_bucket[x][y] == 0:
            ice_bucket[x][y] = label
            dfs(neighbor, ice_bucket, label)


label = 0
for i in range(N):
    for j in range(M):
        if ice_bucket[i][j] == 0:
            dfs([i, j], ice_bucket, 1)
            label += 1


print(ice_bucket)
print(label)
