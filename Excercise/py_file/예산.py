def solution(d, budget):
    answer = 0
    d = sorted(d)
    bud = 0
    for i in d:
        bud += i
        if bud <= budget:
            answer += 1
    return answer