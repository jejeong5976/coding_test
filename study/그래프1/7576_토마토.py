import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split()) #가로,세로

graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 최단거리=최소날짜
def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))
            
    while queue:
        sx,sy = queue.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0<=nx<N and 0<= ny<M and graph[nx][ny]==0:
                graph[nx][ny] = graph[sx][sy] + 1
                queue.append((nx, ny))

bfs()
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            print(-1)
            sys.exit()
        answer = max(answer, graph[i][j])
print(answer-1)