import sys

input = sys.stdin.readline

n,m = map(int, input().split())

data = list(map(int, input().split()))
data.sort() # [10 15 17 19]

# 높이 h 잘린 떡의 합 m
# h는 항상 떡길이의 최대값보다는 작아야함.
# data의 가장 작은값과 큰값의 중간 점을 h로 - 결과 비교후 다시 탐색
def find_h(data, m, start, end):
    if start>end:
        return None
    h = (start+end)//2
    total = 0
    for i in data:
        if i-h>0:
            total+= i-h
    if total==m:
        return h
    elif total<m:
        return find_h(data,m,start,h-1)
    else:
        return find_h(data,m,h+1,end)


print(find_h(data, m, 0, max(data)))