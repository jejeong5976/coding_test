import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

queue = deque([])
for _ in range(N):
    func = list(map(str, input().split()))
    if len(func) == 1:
        if func[0]=='pop_front':
            if len(queue)!=0:
                x = queue.popleft()
                print(x)
            else: print(-1)
        elif func[0]=='pop_back':
            if len(queue)!=0:
                x = queue.pop()
                print(x)
            else: print(-1)
        elif func[0]=='size':
            print(len(queue))
        elif func[0]=='empty':
            print(1 if len(queue)==0 else 0)
        elif func[0]=='front':
            print(queue[0] if len(queue)!=0 else -1)
        elif func[0]=='back':
            print(queue[-1] if len(queue)!=0 else -1)
    else:
        if func[0]=='push_front':
            queue.appendleft(int(func[1]))
        elif func[0]=='push_back':
            queue.append(int(func[1]))
