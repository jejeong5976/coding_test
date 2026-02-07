import sys

n = sys.stdin.readline().strip()

# 8진수 - 2진수
# 2^3진수(3자리씩 슬라이싱) - 2진수 슬라이싱
def change_binary(n):
    list_8 = [
    '000','001','010','011',
    '100','101','110','111'
    ]

    num_str=''
    for i in n:
        num_str = num_str+list_8[int(i)]
    return num_str
print(int(change_binary(n)))

# 내장함수 이용시 더욱 간단하게 해결 가능
# int(n,8): 문자열 n을 8진수로 해석하여 10진수로 변환
# print(bin(int(n, 8))[2:]) #bin 함수(2진수 변환) 이용 시 '0b'가 붙기때문