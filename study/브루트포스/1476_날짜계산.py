import sys
import math

e,s,m = map(int, sys.stdin.readline().split())

# n%15==e, n%28==s, n%19==m
year = s # 조건 하나를 시작값으로 고정 (가장 큰 값일 때 가장 빠름)
while True:
    if (year - e) % 15 == 0 and (year - m) % 19 == 0:
        print(year)
        break
    year += 28