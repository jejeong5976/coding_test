import sys
input = sys.stdin.readline

M = int(input())
S = 0

for i in range(M):
    computation = list(map(str,input().strip().split()))

    if len(computation)==1:
        comp = computation[0]
    else:
        comp, x = computation[0], int(computation[1])
    
    if comp == "add":
        S |= (1 << x) # x번 비트 켜기
    elif comp == "remove":
        S &= ~(1 << x) # x번 비트 끄기
    elif comp == "check":
        print(1 if S & (1 << x) else 0) # x번 비트 확인
    elif comp == "toggle":
        S ^= (1 << x) # x번 비트 뒤집기
    elif comp == "all":
        S = (1 << 21) - 2 # (10..000) -> 최소 21 비트에서(11..111) 마지막 비트만 0으로 (11..110)
    elif comp == "empty":
        S = 0