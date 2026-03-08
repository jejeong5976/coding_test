import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,1,-1,-2,-2,2,2]
dy = [-2,-2,2,2,1,-1,1,-1]

T = int(input())

def bfs(sx,sy,fx,fy):
    queue = deque()
    queue.append((sx,sy,0))
    visited[sx][sy] = True
    
    while queue:
        x,y,count = queue.popleft()
        
        if x==fx and y==fy:
            print(count)
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]            
            if nx<0 or nx>=I or ny<0 or ny>=I:
                continue            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,count+1))

for _ in range(T):
    I = int(input())
    
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    
    visited = [[False]*I for _ in range(I)]
    bfs(sx,sy,fx,fy)
    