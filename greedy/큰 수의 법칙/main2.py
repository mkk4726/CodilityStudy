# 동빈나 풀이

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        result += first
        m -= 1

    result += second
    m -= 1

    if m == 0:
        break

print(result)
