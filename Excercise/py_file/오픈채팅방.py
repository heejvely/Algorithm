def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter','Change']:
            namespace[rr[1]] = rr[2]
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
    
    return answer

def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(f'{dic[sentence_split[1]]}님이 들어왔습니다.')
        elif sentence_split[0] == 'Leave':
            answer.append(f'{dic[sentence_split[1]]}님이 나갔습니다.')
    return answer