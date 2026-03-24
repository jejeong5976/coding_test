import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

dist = [-1] * 100001
parent = [-1] * 100001

def bfs(start):
    queue = deque([start])
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        if cur == K:
            return

        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= 100000 and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                parent[nxt] = cur
                queue.append(nxt)

bfs(N)

print(dist[K])

path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = parent[cur]

print(*path[::-1])