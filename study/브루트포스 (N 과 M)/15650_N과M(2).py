import sys

N, M = map(int, sys.stdin.readline().split())

result = []

def recur(start,depth):
    if depth == M:
        print(' '.join(map(str,result)))
        return
    for i in range(start,N+1):
        result.append(i)
        recur(i+1,depth+1)
        result.pop()
                
recur(1,0)