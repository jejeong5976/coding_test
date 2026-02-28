import sys
input = sys.stdin.readline

N = int(input())
matrix = input().strip()

# 2차원 sign 배열 만들기
sign = [[None]*N for _ in range(N)]

pointer = 0
for i in range(N):
    for j in range(i, N):
        sign[i][j] = matrix[pointer]
        pointer += 1

seq = [0]*N

def check(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += seq[i]
        
        if s > 0 and sign[i][idx] != '+': return False
        if s < 0 and sign[i][idx] != '-': return False
        if s == 0 and sign[i][idx] != '0': return False
    
    return True

def dfs(depth):
    if depth == N:
        print(*seq)
        exit()
    
    # 대각선으로 후보 줄이기
    if sign[depth][depth] == '0':
        seq[depth] = 0
        if check(depth):
            dfs(depth+1)
    elif sign[depth][depth] == '+':
        for num in range(1,11):
            seq[depth] = num
            if check(depth):
                dfs(depth+1)
    else:
        for num in range(-10,0):
            seq[depth] = num
            if check(depth):
                dfs(depth+1)

dfs(0)