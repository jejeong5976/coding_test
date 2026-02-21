import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# a_k-1<=a_k, 중복 O
result = []
def recur(start,depth):
    if depth == M:
        print(*result)
        return
    for i in range(start,len(data)):
        result.append(data[i])
        recur(i,depth+1)
        result.pop()

recur(0,0)