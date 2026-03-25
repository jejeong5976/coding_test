import sys

input = sys.stdin.readline
N = int(input())
tree = {}
is_child = [False] * (N + 1) # 자식 node 체크

for _ in range(N):
    root, left, right = map(int, input().split())
    tree[root] = (left, right)
    if left != -1:
        is_child[left] = True
    if right != -1:
        is_child[right] = True

# 루트 찾기 (자식 노드에서 등장한 적 없는 노드)
root = 0
for i in range(1, N + 1):
    if not is_child[i]:
        root = i
        break

level_min = [10**9] * (N + 1)
level_max = [0] * (N + 1)
x = 0
def dfs(node, depth):
    global x
    if node == -1:
        return
    # 중위 순회
    left, right = tree[node]
    dfs(left, depth + 1)

    x += 1
    level_min[depth] = min(level_min[depth], x)
    level_max[depth] = max(level_max[depth], x)

    dfs(right, depth + 1)

dfs(root, 1)

best_level = 1
best_width = level_max[1] - level_min[1] + 1

for depth in range(2, N + 1):
    if level_max[depth] == 0:
        continue
    width = level_max[depth] - level_min[depth] + 1
    if width > best_width:
        best_width = width
        best_level = depth

print(best_level, best_width)