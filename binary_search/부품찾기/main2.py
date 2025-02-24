# 부품이 N개
# 각 부품은 정수 형태의 고유번호
# M개 종류의 부품을 대량 구매
# 있는지 확인


def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/binary_search/부품찾기/input.txt")

N = int(lines[0].strip())
n_list = list(map(int, lines[1].split()))
M = int(lines[2].strip())
m_list = list(map(int, lines[3].split()))

print(N)
print(n_list)
print(M)
print(m_list)

# 1. 정렬
n_list.sort()
m_list.sort()
print(n_list)
print(m_list)


for m in m_list:
    result = binary_search(n_list, m, 0, len(n_list) - 1)
    if result:
        print("yes", end=" ")
    else:
        print("no", end=" ")
