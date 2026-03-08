import sys
from collections import deque

input = sys.stdin.readline
K = int(input())
# 같은 색의 노드끼리 연결되면 X
def bi_graph(start):
    queue = deque([start])
    color[start] = 1

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if color[nx]==0:
                color[nx] = -color[x] #-1
                queue.append(nx)
            elif color[nx]==color[x]: #인접노드가 같은 색이면 성립 X
                return False

    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [0]*(V+1)
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V+1):
        if color[i]==0:
            if not bi_graph(i):
                print('NO')
                break
    else:
        print('YES')