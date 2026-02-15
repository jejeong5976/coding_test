import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

# max 값 선택 -> max값과 함께 양 옆은 버림-> 존재하는 값중에 max 선택
# a_i = i번째 식량 창고까지의 최적의 해
# k_i = i번째 식량 창고에 있는 식량의 양
# 점화식: a_i = max(a_(i-1), a_(i-2) + k_i)

# dp table 초기화
d = [0]*100

# 보텀업 방식
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+data[i])

print(d[n-1])
