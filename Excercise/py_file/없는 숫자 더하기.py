def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    an = []
    answer = 0
    for i in num:
        if i not in numbers:
            an.append(i)
    for j in an:
        answer += j
    return answer