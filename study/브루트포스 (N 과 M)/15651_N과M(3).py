import sys

N, M = map(int, sys.stdin.readline().split())

result = []

def recur(depth):
    if depth == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1, N+1):
        result.append(i)
        recur(depth+1)
        result.pop()

recur(0)
