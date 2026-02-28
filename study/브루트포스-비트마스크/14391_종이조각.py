import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().strip())) for _ in range(N)]

answer = 0
# 0: 가로, 1: 세로
for mask in range(1 << (N*M)):
    total = 0
    
    for i in range(N):
        cur = 0
        for j in range(M):
            idx = i * M + j # 1차원으로 변환
            if (mask & (1 << idx)) == 0:  # 가로
                cur = cur * 10 + data[i][j]
            else:
                total += cur # 가로 연속이 끝나면 더하기
                cur = 0
        total += cur # 마지막이 가로로 끝나는 경우
    
    for j in range(M):
        cur = 0
        for i in range(N):
            idx = i * M + j
            if (mask & (1 << idx)) != 0:  # 세로
                cur = cur * 10 + data[i][j]
            else:
                total += cur
                cur = 0
        total += cur
    
    answer = max(answer, total)

print(answer)