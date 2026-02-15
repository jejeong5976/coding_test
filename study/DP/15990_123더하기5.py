import sys

input = sys.stdin.readline

t = int(input())

# d: 123의 합으로 나타내는 방법 수
# d[i][j]: i를 만들려고 할 때, j로 끝난 식
d = [[0]*4 for i in range(100001)]
d[1][1] = 1 # 1
d[2][2] = 1 # 2
d[3][1] = 1
d[3][2] = 1
d[3][3] = 1

MOD = 1000000009
for i in range(4,100001):
    d[i][1] = (d[i-1][2]+d[i-1][3]) % MOD
    d[i][2] = (d[i-2][1]+d[i-2][3]) % MOD
    d[i][3] = (d[i-3][1]+d[i-3][2]) % MOD


for _ in range(t):
    n = int(input())
    print(sum(d[n])%MOD)