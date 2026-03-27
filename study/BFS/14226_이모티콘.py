import sys
from collections import deque
S = int(sys.stdin.readline())
# 1. 모든 임티 복사 저장, 2. 모든 임티를 붙여넣기, 3. 이모티콘 삭제
# 최소시간 - BFS

visited = [[False]*2001 for _ in range(2001)]
def bfs():
    queue = deque([])
    queue.append((1,0,0))
    visited[1][0] = True

    while queue:
        count, clip, time = queue.popleft()

        if count == S:
            print(time)
            return 
        
        # 1. copy
        nxt_count = count
        nxt_clip = count
        if not visited[nxt_count][nxt_clip]:
            visited[nxt_count][nxt_clip] = True
            queue.append((nxt_count, nxt_clip, time+1))

        # 2. paste
        if clip > 0:
            nxt_count = count + clip
            nxt_clip = clip
            if 0 <= nxt_count < 2001 and not visited[nxt_count][nxt_clip]:
                visited[nxt_count][nxt_clip] = True
                queue.append((nxt_count, nxt_clip, time+1))

        # 3. delete
        if count > 0:
            nxt_count = count - 1
            nxt_clip = clip
            if not visited[nxt_count][nxt_clip]:
                visited[nxt_count][nxt_clip] = True
                queue.append((nxt_count, nxt_clip, time+1))
                                
bfs()