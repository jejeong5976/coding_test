import sys

n, m = map(int, sys.stdin.readline().split())

result = []
visited = [False]*(n+1)

def recur(n,m,depth):
    if depth == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(n,m,depth+1)
            visited[i] = False
            result.pop()

recur(n,m,0)