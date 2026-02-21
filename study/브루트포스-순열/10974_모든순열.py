import sys

N = int(sys.stdin.readline())

result = []
visited = [False]*(N+1)
def recur(depth):
    if depth == N:
        print(*result)
        return
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(depth+1)
            visited[i] = False
            result.pop()

recur(0)

'''
import sys
from itertools import permutations

N = int(sys.stdin.readline())
data = [i for i in range(1,N+1)]

for p in permutations(data,N):
    print(*p)
'''
