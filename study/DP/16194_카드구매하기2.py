import sys

input = sys.stdin.readline

n = int(input())
pay = list(map(int,input().split()))

# d: i개의 카드를 갖기 위해 지불해야하는 최소 금액
d = [0]*(n+1)
d[1] = pay[0]

for i in range(2,n+1):
    d[i] = pay[i-1]
    for j in range(i):
        d[i] = min(d[i],d[i-j]+d[j])

print(d[n])