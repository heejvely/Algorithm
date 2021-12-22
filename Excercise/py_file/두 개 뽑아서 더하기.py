from itertools import combinations

def solution(numbers):
    answer = []
    li = list(combinations(numbers,2))
    for i in li:
        answer.append(i[0] + i[1])
        answer = sorted(list(set(answer)))
    return answer