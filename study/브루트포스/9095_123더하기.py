import sys

t = int(sys.stdin.readline())

dp = [0] * 12 # n을 만드는 방법 수 저장 (n<=11이므로 12칸)
dp[1]=1
dp[2]=2
dp[3]=4            

for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])