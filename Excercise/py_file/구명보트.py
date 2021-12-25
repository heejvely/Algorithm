def solution(people, limit):
    answer = 0
    per = sorted(people)
    start, end = 0, len(per)-1
    while start <= end:
        if per[start] + per[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer