import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dist = [[float('inf')] * M for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 0

    while queue:
        sx, sy = queue.popleft()

        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                new_cost = dist[sx][sy] + grid[nx][ny]

                if dist[nx][ny] > new_cost:
                    dist[nx][ny] = new_cost
                    if grid[nx][ny] == 0:
                        queue.appendleft((nx, ny))
                    else:
                        queue.append((nx, ny))

bfs()
print(dist[N-1][M-1])