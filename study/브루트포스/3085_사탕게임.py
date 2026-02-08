import sys

# 보드의 크기 n*n
n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 방향 탐색시 오른쪽, 아래쪽만 수행해도 됨 (어차피 중복되기 때문)
# 2방향 탐색시 4방향에 비해 시간이 절반으로 줄어듦
dx=[1, 0]
dy=[0, 1]

def findmax(sx,sy,data):
    count_max=0
    n = len(data)
    for i in range(len(dx)):
        nx = sx+dx[i]
        ny = sy+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        else:
            if data[sx][sy]==data[nx][ny]:
                continue
            else:
                data[sx][sy], data[nx][ny] = data[nx][ny], data[sx][sy]
                count_max = max(
                    count_max,
                    max(count_row_max(data), count_col_max(data))
                )
                data[sx][sy], data[nx][ny] = data[nx][ny], data[sx][sy] #결과 원복
    return count_max

def count_row_max(arr):
    n,m = len(arr),len(arr[0])
    max_count = 0
    for i in range(n):
        count=1
        for j in range(1,m):
            if arr[i][j]==arr[i][j-1]:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1 # count 다시 시작
        max_count=max(max_count,count)
    return max_count

def count_col_max(arr):
    n,m = len(arr), len(arr[0])
    max_count = 0
    for j in range(m):
        count=1
        for i in range(1,n):
            if arr[i][j]==arr[i-1][j]:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1
        max_count=max(max_count,count)
    return max_count

result = 0
for i in range(n):
    for j in range(n):
        result = max(result,findmax(i,j,data))
print(result)