def solution(sizes):
    m = 0
    n = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1],i[0]
        m = max(i[0], m)
        n = max(i[1], n)
    return m * n