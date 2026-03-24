import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

# 최소 이동 시간: BFS
a = [1, 1, 2]
b = [1, -1, 0]
visited = [False]*100_001

def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited[start] = True
    
    while queue:
        cur, count = queue.popleft()

        if cur == K:
            print(count)
            break

        for i in range(3):
            next = a[i] * cur + b[i]           
            if 0<=next<=100_000:
                if not visited[next]:
                    queue.append((next,count+1))
                    visited[next]=True

bfs(N)
