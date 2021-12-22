def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []

    for idx, key in enumerate(answers):
        if key == first[idx%len(first)]:
            score[0] += 1
        if key == second[idx%len(second)]:
            score[1] += 1
        if key == third[idx%len(third)]:
            score[2] += 1
    for idx, key in enumerate(score):
        if key == max(score):
            answer.append(idx + 1)
    return answer