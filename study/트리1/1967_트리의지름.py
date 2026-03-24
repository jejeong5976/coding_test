import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, weight = map(int, input().split())
    graph[u].append((v,weight))
    graph[v].append((u,weight))

def dfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    stack = [(start, 0)]
    far_node = start
    far_dist = 0

    while stack:
        node, dist = stack.pop()
        if dist > far_dist:
            far_dist = dist
            far_node = node

        for nxt, w in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, dist + w))

    return far_node, far_dist

a, _ = dfs(1)
_, diameter = dfs(a)
print(diameter)