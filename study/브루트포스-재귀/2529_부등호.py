import sys

input = sys.stdin.readline
K = int(input())
data = list(map(str,input().split()))

visited = [False]*10
result = []
total = []
def dfs(depth):
    global total
    if depth==K+1:
        total.append(''.join(map(str,result[:])))
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0:
                visited[i]=True
                result.append(i)
                dfs(depth+1)
                visited[i]=False
                result.pop()
            else:
                if data[depth-1]=='<' and result[-1]<i:
                    visited[i]=True
                    result.append(i)
                    dfs(depth+1)
                    visited[i]=False
                    result.pop()
                elif data[depth - 1] == '>' and result[-1]>i:
                    visited[i]=True
                    result.append(i)
                    dfs(depth+1)
                    visited[i]=False
                    result.pop()

dfs(0)
total.sort()
print(max(total))
print(min(total))