import sys
input = sys.stdin.readline

N = int(input())
tp = [list(map(int, input().split())) for _ in range(N)]

dp = [-1] * (N+1) # 버는 돈의 최대값

def solution(day):
    if day >= N:
        return 0

    if dp[day] != -1:
        return dp[day]

    if day + tp[day][0] <= N:
        take = tp[day][1] + solution(day+tp[day][0])
    else:
        take = 0
    skip = solution(day+1) # 상담 안하는 경우

    dp[day] = max(take, skip)

    return dp[day]

print(solution(0))