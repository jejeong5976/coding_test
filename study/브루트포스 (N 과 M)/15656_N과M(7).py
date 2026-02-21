import sys

input = sys.stdin.readline
N,M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

# 중복 O, 수열
result = []
def recur(depth):
    if depth == M:
        print(' '.join(map(str,result))) # print(*result)
        return
    for i in range(len(data)):
        result.append(data[i])
        recur(depth+1)
        result.pop()

recur(0)