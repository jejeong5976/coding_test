import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n,x = map(int, input().split())

data = list(map(int,input().split()))

def x_count(data,x):
    if x not in data:
        return -1
    return bisect_right(data,x)-bisect_left(data,x)

print(x_count(data,x))