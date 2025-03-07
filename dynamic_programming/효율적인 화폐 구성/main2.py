# 동빈나 풀이

def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/dynamic_programming/효율적인 화폐 구성/input2.txt")

N, M = map(int, lines[0].split())
money_list = []
for line in lines[1:]:
    money_list.append(int(line))
    
print(N, M)
print(money_list)

d = [100001] * (M + 1)

d[0] = 0    
for i in range(N):
    for j in range(money_list[i], M + 1):
        if d[j - money_list[i]] != 100001:
            d[j] = min(d[j], d[j - money_list[i]] + 1)

if d[M] == 100001:
    print(-1)
else:
    print(d[M])
    
    