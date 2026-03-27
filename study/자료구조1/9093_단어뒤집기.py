import sys

input = sys.stdin.readline
T = int(input())

def reverse(data):
    result = []
    for s in data:
        result.append(s[::-1])
    return result

for _ in range(T):
    data = list(map(str, input().split()))
    print(*reverse(data))