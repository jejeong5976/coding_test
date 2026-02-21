import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = []
visited = [False]*N
# 중복X, 순열
def recur(depth):
    if depth == M:
        print(' '.join(map(str,result)))
    for i in range(0,N):
        if visited[i]==False:
            visited[i]=True
            result.append(data[i])
            recur(depth+1)
            visited[i]=False
            result.pop()

recur(0)