def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


lines = read_txt_lines("/Users/user/Desktop/CodilityStudy/dynamic_programming/개미전사/input.txt")

N = int(lines[0])
data_list = list(map(int, lines[1].split()))

print(N)
print(data_list)

max_data_list = [0] * (N + 1)
max_data_list[0] = data_list[0]
max_data_list[1] = data_list[1]

for i in range(2, N):
    max_data = max(data_list[i] + max_data_list[i-2], max_data_list[i-1])
    max_data_list[i] = max_data

print(max_data_list[N - 1])
print(max_data_list)