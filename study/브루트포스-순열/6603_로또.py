import sys
from itertools import combinations

input = sys.stdin.readline

while True:    
    data = list(map(int,input().split()))
    if data[0]==0:
        break
    k, s = data[0], data[1:]
    for c in combinations(s,6):
        print(*c)
    print()