import sys

input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

# 합이 S가 되도록 하는 집합 찾기
count = 0

def dfs(idx, total):
    global count

    if idx == N:
        if total == S:
            count += 1
        return
    dfs(idx + 1, total) # 선택 안하는 경우
    dfs(idx + 1, total + array[idx]) # 선택 하는 경우

dfs(0, 0)

if S == 0:
    count -= 1

print(count)