import sys

H, W, N, M = map(int, sys.stdin.readline().split())

r = (W-1) // (M+1) + 1
c = (H-1) // (N+1) + 1
print(r*c)