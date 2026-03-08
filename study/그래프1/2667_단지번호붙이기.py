import sys

input = sys.stdin.readline
N = int(input())
grid = [list(map(int,input().strip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*N for _ in range(N)]

def dfs(sx,sy):
    visited[sx][sy]=True
    count = 1
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if not visited[nx][ny] and grid[nx][ny]==1:
            count += dfs(nx,ny)
    return count

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j]==1:
            result.append(dfs(i,j))

result.sort()
print(len(result))
for r in result:
    print(r)

