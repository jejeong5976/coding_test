import sys

n,m = map(int,sys.stdin.readline().split())

# nCm = n!/m!(n-m)!
# 0의 개수는 10 = 2*5 의 개수
def check_num(x,a):
    count = 0
    while x>0:
        x//=a
        count+=x
    return count

total_2 = check_num(n,2)-check_num(m,2)-check_num(n-m,2)
total_5 = check_num(n,5)-check_num(m,5)-check_num(n-m,5)

print(min(total_2,total_5))