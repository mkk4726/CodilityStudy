cur_loc = input()

# 좌표로 바꾸기
x_loc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

x, y = x_loc[cur_loc[0]], int(cur_loc[1])

print(cur_loc)
print(x, y)

dx = [-2, 2, -1, 1]
dy = [-1, 1, -2, 2]

# 움직이는 경우의 수
# 수평으로 2칸 이동 -> 수직 1칸 이동
# 수직으로 2칸 이동 -> 수평 1칸 이동
total_cnt = 0

for i in range(2):
    for j in range(2):
        tmp_x = x + dx[i]
        tmp_y = y + dy[j]

        if 1 <= tmp_x <= 8 and 1 <= tmp_y <= 8:
            print(dx[i], dy[i], tmp_x, tmp_y)
            total_cnt += 1

for i in range(2, 4):
    for j in range(2, 4):
        tmp_x = x + dx[i]
        tmp_y = y + dy[j]

        if 1 <= tmp_x <= 8 and 1 <= tmp_y <= 8:
            print(dx[i], dy[i], tmp_x, tmp_y)
            total_cnt += 1

print(total_cnt)
