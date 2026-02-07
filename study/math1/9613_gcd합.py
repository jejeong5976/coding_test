import sys
import math
from itertools import combinations
t = int(sys.stdin.readline())

def gcd_sum(data):
    answer = 0
    for i in combinations(data,2):
        answer+=math.gcd(i[0],i[1])
    return answer

for _ in range(t):
    data= list(map(int,sys.stdin.readline().split()))
    print(gcd_sum(data[1:]))
