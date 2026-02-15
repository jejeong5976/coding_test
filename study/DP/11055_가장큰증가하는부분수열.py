import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))

dp_sum = [0]*n
dp_sum[0] = array[0]

for i in range(1,n):
    dp_sum[i] = array[i]
    for j in range(i):
        if array[i]>array[j]:
            dp_sum[i] = max(dp_sum[i],dp_sum[j]+array[i])

print(max(dp_sum))