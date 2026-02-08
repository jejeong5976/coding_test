import sys
from itertools import combinations

# input
height=[int(sys.stdin.readline()) for _ in range(9)]

for i in combinations(height,7):
    if sum(i)==100:
        answer=sorted(list(i))
        for j in answer:
            print(j)
        break