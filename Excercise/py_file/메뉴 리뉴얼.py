from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for num in course:
        menu = []
        for i in orders:
            combi = combinations(sorted(i), num)
            menu += combi
        a = Counter(menu)
        if a:
            max_ = max(list(a.values()))
            if max_ >= 2:
                for key, value in a.items():
                    if a[key] == max_:
                        answer.append(''.join(key))
    return sorted(answer)