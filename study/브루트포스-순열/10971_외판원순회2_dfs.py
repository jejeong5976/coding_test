import sys
input = sys.stdin.readline

N = int(input())
pay = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = float('inf')

def dfs(city, depth, total):
    global result
    
    if total >= result: # 가지치기
        return
    
    if depth == N:
        if pay[city][0] != 0:
            result = min(result, total + pay[city][0])
        return
    
    for next_city in range(1, N):  # 0은 시작점이므로 제외
        if visited[next_city]==False and pay[city][next_city] != 0:
            visited[next_city] = True
            dfs(next_city, depth + 1, total + pay[city][next_city])
            visited[next_city] = False

visited[0] = True
dfs(0, 1, 0)
print(result)