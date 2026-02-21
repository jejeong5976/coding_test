import sys

input = sys.stdin.readline
N, M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

result = []
def recur(start,depth):
    if depth == M:
        print(*result)
        return 
    prev = -1
    for i in range(start,len(data)):
        if data[i] != prev:
            result.append(data[i])
            prev = data[i]
            recur(i+1,depth+1)
            result.pop()

recur(0,0)