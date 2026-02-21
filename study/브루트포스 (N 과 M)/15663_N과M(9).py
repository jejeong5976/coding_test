import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 중복 X, 순열
result = []
visited = [False]*N
def recur(depth):
    if depth == M:
        print(*result)
        return 
    prev = -1
    for i in range(len(data)):
        if visited[i]==False and data[i] != prev:
            visited[i]=True
            result.append(data[i])
            prev = data[i]
            recur(depth+1)
            visited[i]=False
            result.pop()

recur(0)