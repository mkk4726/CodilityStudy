
# 재귀식 
# O(2^N)
def fibo(x):
    if x in [1, 2]:
        return 1
    return fibo(x-1) + fibo(x-2)

# memoization 적용
# O(N)
d = [0] * 100

def fibo(x):
    if x in [1, 2]:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo[x-1] + fibo[x-2]

    return d[x]

# bottom-up
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]

print(d[n])