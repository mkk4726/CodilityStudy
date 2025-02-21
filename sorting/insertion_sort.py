array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 왼쪽은 이미 정렬이 되었다고 가정
# 새로운 값을 정렬이 되어있는 곳 중 어디에 넣으면 될까?를 반복
# 바로 옆에 있는 값이랑만 비교하면서 더 작으면 자리 바꿈
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
