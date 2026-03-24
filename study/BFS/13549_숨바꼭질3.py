import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dist = [10**9] * 100001

def bfs(start):
    queue = deque()
    queue.append(start)
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        nxt = cur * 2
        if 0 <= nxt <= 100000 and dist[nxt] > dist[cur]:
            dist[nxt] = dist[cur] # 시간 증가 X
            queue.appendleft(nxt) # 0초 이동 - 먼저 처리

        nxt = cur - 1
        if 0 <= nxt <= 100000 and dist[nxt] > dist[cur] + 1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)

        nxt = cur + 1
        if 0 <= nxt <= 100000 and dist[nxt] > dist[cur] + 1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)

    print(dist[K])

bfs(N)