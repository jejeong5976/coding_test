import sys

n = int(sys.stdin.readline())

# d: 계단수의 개수
d = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    d[1][i] = 1
# d[2] = 17->10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98
MOD = 1000000000
for i in range(2,n+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for j in range(1,9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % MOD

print(sum(d[n])%MOD)