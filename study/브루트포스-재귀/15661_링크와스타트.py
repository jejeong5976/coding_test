import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = float("inf")

def dfs(idx):
    global result
    
    if idx == N:
        team1 = []
        team2 = []
        
        for i in range(N):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        
        if len(team1) == 0 or len(team2) == 0:
            return
        
        sum1 = 0
        sum2 = 0        
        for i in range(len(team1)):
            for j in range(i+1, len(team1)):
                a = team1[i]
                b = team1[j]
                sum1 += S[a][b] + S[b][a]
        
        for i in range(len(team2)):
            for j in range(i+1, len(team2)):
                a = team2[i]
                b = team2[j]
                sum2 += S[a][b] + S[b][a]
        
        result = min(result, abs(sum1 - sum2))
        return

    visited[idx] = True
    dfs(idx + 1)

    visited[idx] = False
    dfs(idx + 1)

visited[0] = True
dfs(1)
print(result)