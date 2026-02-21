import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

def next_permutation(data):
    i = N-1
    while i>0 and data[i-1] >= data[i]: #뒤부터 확인
        i -= 1
    if i == 0: # 완전 역순인 경우
        return None
    j = N - 1
    while data[i-1] >= data[j]: # pivot보다 큰 값중 가장 작은 값
        j -= 1

    data[i-1], data[j] = data[j], data[i-1] # swap
    data[i:] = reversed(data[i:])

    return data

res = next_permutation(data)

if res is None:
    print(-1)
else:
    print(*res)