import sys

input = sys.stdin.readline

t = int(input())

# d: 스티커 점수의 최댓값
# d[선택 row][컬럼]
def max_score(n, score):
    if n == 1:
        return max(score[0][0], score[1][0])
    
    d = [[0]*n for _ in range(2)]

    d[0][0] = score[0][0]
    d[1][0] = score[1][0]

    d[0][1] = score[0][1] + d[1][0]
    d[1][1] = score[1][1] + d[0][0]

    for i in range(2, n):
        # 이전 컬럼에서 아무것도 안고르는 경우를 고려하여 i-2를 계산에 포함
        d[0][i] = max(d[1][i-1], d[1][i-2]) + score[0][i]
        d[1][i] = max(d[0][i-1], d[0][i-2]) + score[1][i]

    return max(d[0][n-1], d[1][n-1])


for _ in range(t):
    n = int(input())
    score=[]
    for _ in range(2):
        score.append(list(map(int,input().split())))
    print(max_score(n,score))