import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

def prev_permutation(data):
    i = N-1
    while i>0 and data[i-1]<=data[i]: 
        i-=1
    if i==0:
        return None
    j = N-1
    while data[i-1]<=data[j]: # pivot보다 가장 큰 작은 값
        j-=1
    
    data[i-1], data[j] = data[j], data[i-1]
    data[i:] = reversed(data[i:])
    return data

res = prev_permutation(data)

if res==None:
    print(-1)
else:
    print(*res)