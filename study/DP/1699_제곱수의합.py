import sys

n = int(sys.stdin.readline())

d = [0]*(n+1)
d[1] = 1
if n>=2:
    d[2] = 2

for i in range(3,n+1):
    d[i] = i    # 최악의 경우 1로만 구성
    j=1
    while j*j<=i:
        d[i] = min(d[i],d[i-j*j]+1)
        j+=1

print(d[n])
