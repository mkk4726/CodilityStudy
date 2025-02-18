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


lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/implementation/상하좌우/input.txt")

N = int(lines[0].strip())
planner = lines[1].split(" ")

print(N)
print(planner)

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plain in planner:
    for i in range(len(move_types)):
        if 
