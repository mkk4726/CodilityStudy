def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines

lines = read_txt_lines("/Users/user/Desktop/CodilityStudy/binary_search/떡볶이 떡 만들기/input.txt")

N, M = map(int, lines[0].split())
data_list = list(map(int, lines[1].split()))

print(N, M)
print(data_list)

# H의 범위 정해주기
max_H = max(data_list)
min_H = 0

# min_H ~ max_H 까지 이진탐색
def count_M(H, data_list):
    return sum([max(data - H, 0) for data in data_list])



start = min_H
end = max_H

max_H = 0
while True:
    if start >= end:
        break    

    H = (start + end) // 2
    max_H = max(max_H, H)
    if count_M(H, data_list) >= M:
        start = H + 1
    else:
        end = H - 1    


print("Max H:", H)