import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 중복 X, 조합
result = []
def recur(start, depth):
    if depth == M:
        print(' '.join(map(str,result)))
        return
    for i in range(start,len(data)):
        result.append(data[i])
        recur(i+1, depth+1)
        result.pop()

recur(0,0)