def solution(n):
    answer = n + 1
    cri = format(n,'b').count(1)
    while True:
        a = format(answer,b).count(1)
        if (answer > n) and (cri == a):
            break
        else:
            answer += 1
    return answer