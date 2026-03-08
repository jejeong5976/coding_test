import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for v in range(1, len(graph)):
	graph[v].sort()
     
def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
         v = queue.popleft()
         print(v, end=' ')
         for i in graph[v]:
              if not visited[i]:
                   queue.append(i)
                   visited[i]=True

dfs(graph,V,[False]*(N+1))
print()
bfs(graph,V,[False]*(N+1))