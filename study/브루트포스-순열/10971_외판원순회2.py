import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
pay = [list(map(int,input().split())) for _ in range(N)]

'''
시작점은 다르지만 경로가 결국 동일 -> 중복 제거: 시작 도시 고정
0 - 1 - 2 - 3 - 0
1 - 2 - 3 - 0 - 1
2 - 3 - 0 - 1 - 2
'''
result = float('inf')
for p in permutations(range(1,N)):
    total = 0
    prev = 0 # 시작 도시를 0으로 고정
    flag = True

    for next in p:
        if pay[prev][next]==0:
            flag=False
            break
        total+=pay[prev][next]
        prev = next

    if not flag:
        continue

    if pay[prev][0]==0:
        continue

    total += pay[prev][0]
    result = min(result,total)

print(result)