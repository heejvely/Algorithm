def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i , priority in enumerate(priorities):
            s = search[c]
            if s == priority:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer

from collections import deque
def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer