import sys
import os

# 현재 파일이 위치한 디렉토리
current_dir = os.path.dirname(os.path.abspath(__file__))

# 상위 폴더 (한 단계 위)
parent_dir = os.path.dirname(current_dir)

# 상위 폴더의 상위 폴더 (두 단계 위)
grandparent_dir = os.path.dirname(parent_dir)

# sys.path에 추가
sys.path.append(grandparent_dir)

from utils import read_txt_lines

lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/implementation/게임개발/input.txt")

N, M = map(int, lines[0].split())  # 맵 크기
A, B, d = map(int, lines[1].split())  # 캐릭터의 위치, 바라보는 곳. 0: 북쪽. 1: 동쪽. 2: 남쪽. 3: 서쪽.
map_list = []  # 맵에 대한 정보. 0: 육지. 1: 바다
for line in lines[2:]:
    map_list.append(list(map(int, line.split())))
print(N, M)
print(A, B, d)
print(map_list)

# 이미 가본 칸이거나 바다면 갈 수 없음
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로만 회전만 수행하고 1단계로 돌아간다.
# 3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한채로 한 칸 뒤로 가고 1단계로 돌아감.
# (뒤쪽 방향이 바다면 움직임을 멈춤)

# 캐릭터 현재 위치
x, y, d = A, B, d

# 캐릭터의 왼쪽방향 좌표 가져오기
moves = {0: [-1, 0], 1: [0, +1], 2: [+1, 0], 3: [0, -1]}

seen_maps = []
cnt_d = 0  # 4방향 모두 탐색했는지 확인용
cnt_moved_maps = 0  # 방문한 칸의 개수
while True:
    # 왼쪽 방향갈 수 있는지 확인
    d = 3 if d == 0 else d - 1
    move = moves[d]
    moved_x, moved_y = x + move[0], y + move[1]
    cnt_d += 1
    # 가본 곳인지, 바다인지, 맵 바깥 쪽인지 확인
    if [moved_x, moved_y] in seen_maps or map_list[moved_x][moved_y] or moved_x < 1 or moved_x > N or moved_y < 1 or moved_y > M:
        if cnt_d == 4:
            moved_x, moved_y = x - move[0], y - move[1]

            if map_list[moved_x][moved_y] == 1:  # 바다면 종료
                break
            else:
                x, y = moved_x, moved_y
                cnt_d = 0
        else:
            continue
    else:
        x, y = moved_x, moved_y
        cnt_moved_maps += 1
        cnt_d = 0
        seen_maps.append([x, y])

print(cnt_moved_maps)
