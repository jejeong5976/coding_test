import sys

input = sys.stdin.readline
N, M = map(int,input().split())
dots = [list(map(str,input().strip())) for _ in range(N)]

# dfs
visited = [[False]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(sx,sy,px,py,color): # px,py: 이전 좌표
    if visited[sx][sy]: # 사이클 발견
        return True
    
    visited[sx][sy]=True

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0<=nx<N and 0<=ny<M and dots[nx][ny]==color:
            if nx==px and ny==py:
                continue
            if dfs(nx,ny,sx,sy,color):
                return True
            
    return False


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if dfs(i,j,-1,-1,dots[i][j]):
                print("Yes")
                sys.exit()
else:
    print("No")

