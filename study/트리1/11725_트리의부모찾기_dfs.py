import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1) # visited와 부모노드 기록을 동시에

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    for nxt in graph[node]: # node의 인접 노드 체크
        if parent[nxt] == 0: # 기록 없으면 해당 노드를 루트로
            parent[nxt] = node
            dfs(nxt)

parent[1] = -1 # root
dfs(1)
for i in range(2,N+1):
    print(parent[i])
