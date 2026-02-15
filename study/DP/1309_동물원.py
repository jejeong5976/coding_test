import sys

n = int(sys.stdin.readline())

# d[i][j]: 2*i번째 배열을 채울 때, i-1번째 배열의 경우 j
# j: 배치하지 않는 경우 0, 첫번째 col은 1, 두번째 col 2
d = [[0]*3 for _ in range(n+1)]

for i in range(3):
    d[1][i] = 1

MOD = 9901
for i in range(2,n+1):
    d[i][0] = sum(d[i-1]) % MOD
    d[i][1] = d[i-1][0]+d[i-1][2] % MOD
    d[i][2] = d[i-1][0]+d[i-1][1] % MOD

print(sum(d[n]) % MOD)