import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0]*(N+1)
parent[1] = -1
queue = deque([1])
while queue:
    node = queue.popleft()
    for nxt in graph[node]:
        if parent[nxt] == 0:
            parent[nxt] = node
            queue.append(nxt)

print('\n'.join(map(str,parent[2:])))
