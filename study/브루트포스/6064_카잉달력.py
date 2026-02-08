import sys
import math

t = int(sys.stdin.readline())

def mn(m,n,x,y):
    year=x
    lcm = m*n//math.gcd(m,n)
    while year<=lcm:
        if (year-y)%n==0:
            print(year)
            return
        year+=m
    print(-1)
    

for _ in range(t):
    m,n,x,y = map(int, sys.stdin.readline().split())
    mn(m,n,x,y)