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

max_loc = [5, 5]
current_loc = [1, 1]

for plan in planner:
    match plan:
        case "L":
            if 1 <= current_loc[1] - 1 <= max_loc[0]:
                current_loc[1] -= 1
        case "R":
            if 1 <= current_loc[1] + 1 <= max_loc[0]:
                current_loc[1] += 1
        case "U":
            if 1 <= current_loc[0] - 1 <= max_loc[1]:
                current_loc[0] -= 1
        case "D":
            if 1 <= current_loc[0] + 1 <= max_loc[0]:
                current_loc[0] += 1

print(current_loc)
