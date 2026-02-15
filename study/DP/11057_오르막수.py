import sys

n = int(sys.stdin.readline())
MOD = 10007

# d: 오르막 수의 개수
# i = n, j: 끝자리 수
d = [[0]*10 for _ in range(n+1)]

for i in range(10):
    d[1][i] = 1 # 0~9

for i in range(2,n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][0:j+1]) % MOD

print(sum(d[n]) % MOD)