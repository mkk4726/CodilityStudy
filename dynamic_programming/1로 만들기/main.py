def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


lines = read_txt_lines("/Users/user/Desktop/CodilityStudy/dynamic_programming/1로 만들기/input.txt")

X = int(lines[0])

print(X)

count_list = [0] * (X + 1)
count_list[1] = 0
count_list[2] = 0

for N in range(3, X + 1):
    min_count = X
    if N % 5 == 0:
        min_count = min(count_list[N // 5] + 1, min_count)
    
    if N % 3 == 0:
        min_count = min(count_list[N // 3] + 1, min_count)
    
    if N % 2 == 0:
        min_count = min(count_list[N // 2] + 1, min_count)
    
    min_count = min(count_list[N - 1] + 1, min_count)
    
    count_list[N] = min_count
    
print(count_list[X])