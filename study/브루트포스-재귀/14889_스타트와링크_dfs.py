import sys

input = sys.stdin.readline
N = int(input())
s_ij = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = float("inf")

def dfs(start,depth):
    global result
    team1 = 0
    team2 = 0
    if depth == N//2:
        for i in range(N):
            for j in range(i+1,N):
                if visited[i] and visited[j]:
                    team1 += (s_ij[i][j]+s_ij[j][i])
                elif not visited[i] and not visited[j]:
                    team2 += (s_ij[i][j]+s_ij[j][i])
        result = min(result,abs(team1-team2))
        return 
    
    for i in range(start,N):
        if not visited[i]:
            visited[i]=True
            dfs(i+1,depth+1)
            visited[i]=False

visited[0] = True # 대칭 제거 - 0번은 무조건 team1로 설정
dfs(1,1) # 0을 team1로 함으로써 이미 depth=1 상태
print(result)