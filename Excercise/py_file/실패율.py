def solution(N, stages):
    result = {}
    a = len(stages)
    for stage in range(1, N+1):
        if a != 0:
            count = stages.count(stage)
            result[stage] = count/a
            a -= count
        else:
            result[stage] = 0
    return sorted(result, lambda x : result[x], reverse=True)