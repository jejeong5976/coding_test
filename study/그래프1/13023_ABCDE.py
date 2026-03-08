import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
flag = False
def dfs(v, depth):
    global flag
    if depth == 5:
        flag = True
        return
    for i in graph[v]:
        if not visited[i]:
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False

for i in range(1,N+1):
    visited[i] = True
    dfs(i,1)
    visited[i] = False
    if flag:
        break
print(1 if flag else 0)
