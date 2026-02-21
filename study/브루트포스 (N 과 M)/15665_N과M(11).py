import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 중복 O, 순열
result = []
def recur(depth):
    if depth == M:
        print(*result)
        return
    prev = -1
    for i in range(len(data)):
        if data[i] != prev:
            result.append(data[i])
            prev = data[i]
            recur(depth+1)
            result.pop()

recur(0)