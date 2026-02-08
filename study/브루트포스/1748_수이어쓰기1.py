import sys

n=int(sys.stdin.readline())

length = len(str(n))
result = 0

for i in range(1, length):
    result += 9 * (10**(i-1)) * i

# 마지막 자리수
result += (n - 10**(length-1) + 1) * length

print(result)