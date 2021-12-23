def solution(s):
    answer = ''
    for i in s.split(' '):
        i = i.capitalize()
        answer += f' {i}'
    return answer[1:]