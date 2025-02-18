# 시간복잡도 더 줄인 풀이

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# first, second 몇번 더할지
# first는 cnt * k번 + rest 번
# second는 cnt번
cnt = m // (k + 1)
rest = m % (k + 1)

total = 0

total += first * ((cnt * k) + rest)
total += second * cnt

print(total)
