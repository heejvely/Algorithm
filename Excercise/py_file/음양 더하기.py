def solution(absolutes, signs):
    answer = 0
    for idx, i in enumerate(absolutes):
        if signs[idx] == True:
            answer += i
        if signs[idx] == False:
            answer -= i
    return answer