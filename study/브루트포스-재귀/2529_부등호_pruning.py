import sys
input = sys.stdin.readline

K = int(input())
data = input().split()

def solve(order):
    visited = [False] * 10
    result = []
    answer = None

    def dfs(depth):
        nonlocal answer
        if answer:
            return
        
        if depth == K + 1:
            answer = ''.join(map(str, result))
            return
        
        for i in order:
            if not visited[i]:
                if depth == 0 or \
                   (data[depth-1] == '<' and result[-1] < i) or \
                   (data[depth-1] == '>' and result[-1] > i):
                    
                    visited[i] = True
                    result.append(i)
                    dfs(depth + 1)
                    result.pop()
                    visited[i] = False
    
    dfs(0)
    return answer

print(solve(range(9, -1, -1)))  # 최대
print(solve(range(10)))         # 최소