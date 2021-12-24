def convert(num, base):
    temp = '0123456789ABCEF'
    q,r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q,base) + temp[r]

def solution(n,t,m,p):
    answer = ''
    i = 0
    while len(answer) < m*t:
        answer += convert(i,n)
        i += 1
    return answer[p-1::m][:t]