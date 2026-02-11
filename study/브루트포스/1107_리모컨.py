import sys

input = sys.stdin.readline
n = int(input()) #희망 채널
m = int(input()) #고장난 버튼수
no_buttons=[]
if m>0:
    no_buttons=list(map(int,input().split()))


# 버튼이 고장나지 않은 경우 - 그냥 button or 100근처면 +-
# 버튼이 고장난경우 가장 가까운 숫자

def check_channel(n):
    for i in str(n):
        if int(i) in no_buttons:
            return False
    return True


result = abs(n - 100)
for x in range(0, 1_000_000):
    if check_channel(x):
        presses = len(str(x)) + abs(n - x)
        result = min(result, presses)
print(result)