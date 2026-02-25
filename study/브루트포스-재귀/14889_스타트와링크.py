import sys
from itertools import combinations,combinations_with_replacement
input = sys.stdin.readline
N = int(input())
s_ij = [list(map(int, input().split())) for _ in range(N)]

# 중복 X 조합 group 2
result = float("inf")

for team1 in combinations(range(N),N//2):
    score1 = 0
    score2 = 0
    team2 = [i for i in range(N) if i not in team1]
    
    for i,j in combinations_with_replacement(team1,2):
        score1 += (s_ij[i][j] + s_ij[j][i])
    for i,j in combinations_with_replacement(team2,2):
        score2 += (s_ij[i][j] + s_ij[j][i])

    result = min(result, abs(score1-score2))

print(result)