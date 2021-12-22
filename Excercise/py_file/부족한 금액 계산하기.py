def solution(price, money, count):
    mon = 0
    for i in range(1, count+1):
        mon += i * price
    if mon >= money:
        answer = mon - money
    else:
        answer = 0
    return answer