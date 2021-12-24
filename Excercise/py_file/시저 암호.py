def solution(s, n):
    temp = 'abcdefghijklmnopqrstuvwxyz'
    temp2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for i in s:
        if i in temp:
            if (temp.find(i) + n) > len(temp):
                answer += temp[temp.find(i)+n -len(temp)]
            else:
                answer += temp[temp.find(i)+n]
        elif i == ' ':
            answer += ' '
        elif i in temp2:
            if (temp2.find(i) + n) > len(temp2):
                answer += temp2[temp2.find(i)+n -len(temp2)]
            else:
                answer += temp2[temp2.find(i)+n]
    return answer