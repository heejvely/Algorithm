# 10진수를 n진수로 바꾸는 함수
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += mod
    return rev_base[::-1] # 역순으로 뒤집어줘야 n진수고 변경됨

# n진수를 10진수로 변경하는 법
def make(num, n):
    return int(num, n)