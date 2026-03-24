import sys

input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1,len(data),2):
        if data[i] == -1:
            break
        nxt, w = data[i], data[i + 1]
        graph[node].append((nxt, w))

def dfs(start):
    visited = [False]*(V+1)
    visited[start] = True
    far_node = start
    far_dist = 0
    stack = [(start,0)]

    while stack:
        node, dist = stack.pop()
        if far_dist < dist:
            far_dist = dist
            far_node = node

        for nxt,w in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt,dist+w))
    return far_node, far_dist

far_node, _ = dfs(1)
_, result = dfs(far_node)
print(result)