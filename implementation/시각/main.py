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

lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/implementation/시각/input.txt")

N = int(lines[0].strip())

# 00시 00분 00초 ~ N시 59분 59초.
# 3이 하나라도 포함된 모든 경우의 수

# 3중 for문?
total_cnt = 0
for hour in range(N + 1):

    for minute in range(60):
        minute = str(minute)

        for second in range(60):
            second = str(second)

            clock = f"{hour}-{minute}-{second}"
            if "3" in clock:
                total_cnt += 1

print(total_cnt)
