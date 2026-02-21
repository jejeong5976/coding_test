import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

result = 0

for p in permutations(data):
    total = 0
    for i in range(N-1):
        total += abs(p[i]-p[i+1])
    result = max(result,total)

print(result)