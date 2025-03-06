def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines


lines = read_txt_lines("/Users/user/Desktop/CodilityStudy/dynamic_programming/1로 만들기/input.txt")

X = int(lines[0])

print(X)

count = 0
while X != 1:
    if X % 5 == 0:
        print('split 5')
        X /= 5
        count +=1
    elif X % 3 == 0:
        print('split 3')
        X /= 3
        count +=1
    elif X % 2 == 0:
        print('split 2')
        X /= 2
        count += 1
    else:
        print('minus 5')
        X -= 1
        count += 1

print(count)