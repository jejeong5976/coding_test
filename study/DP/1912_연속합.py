import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))

d = [0]*n
d[0] = data[0]

# d: 합 정보
# 이전 합 + 현재 합 or 현재 합 중에 최댓값 선택
for i in range(1,n):
    d[i] = max(d[i-1]+data[i], data[i])

print(max(d))