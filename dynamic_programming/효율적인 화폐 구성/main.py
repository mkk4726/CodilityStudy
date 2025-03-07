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

d = [-1] * (100)

for money in money_list:
    d[money] = 1
    
for i in range(1, M+1):
    count_list = []
    for money in money_list:
        if i >= money and d[i - money] > 0:
            count_list.append(d[i - money] + 1) 

    if len(count_list) != 0:
        d[i] = min(count_list)
        

print(d)
print(d[M])