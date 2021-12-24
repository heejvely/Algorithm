def solution(x):
    answer = 0
    for i in range(len(str(x))):
        answer += int(str(x)[i])
    if x % answer == 0:
        return True
    else:
        return False