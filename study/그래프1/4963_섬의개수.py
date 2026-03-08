import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
def dfs(sx,sy):
    visited[sx][sy]=True
    count=1
    for i in range(8):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx<0 or nx>=H or ny<0 or ny>=W:
            continue
        if not visited[nx][ny] and grid[nx][ny]==1: 
            dfs(nx,ny)

while True:
    W,H = map(int,input().split())
    if W==0 and H==0:
        break
    grid = [list(map(int,input().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and grid[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)