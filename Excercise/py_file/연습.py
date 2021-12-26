
"""로또 최고 최저 등수"""
def solution(lottos,win_num):
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    answer = 0
    for i in lottos:
        if i in win_num:
            answer+= i
    return rank[answer+cnt], rank[answer]

"""추천 아이디"""
import re
def solution(new_id):
    id = new_id.lower()
    id = re.sub('[^a-z0-9\-_.]','',id)
    id = re.sub('[\.]+','.',id)
    id = re.sub('^[\.]|[\.]$','',id)
    if len(id) == 0:
        id = 'a'
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = re.sub('\.$','',id)
    while len(id) <= 2:
        id = id + id[-1]
        if len(id) == 3:
            break
    return id

def solution(new_id):
    new_id = new_id.lower()
    import re
    new_id = re.sub('[^a-z0-9\-_.]','',new_id)
    new_id = re.sub('\.+','.',new_id)
    new_id = re.sub('^[\.]|[\.]$','',new_id)
    if len(new_id) == 0:
        new_id = re.sub('','a',new_id)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$','',new_id)
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
        if len(new_id) == 3:
            break
    return new_id

"""숫자 문자열과 영단어"""
def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx, n in enumerate(num):
        if n in s:
            s = s.replace(n,str(idx))
    return int(s)

"""키패드 누르기"""
# 다음 위치 키패드의 거리 구하기
def get_distance(keypad, finger_position, next_number):
    next_number_position = keypad[next_number]
    distance = abs(finger_position[0] - next_number_position[0]) + abs(finger_position[1] - next_number_position[1])
    return distance

# result 구하기
def solution(numbers, hand):
    result = ''
    #keypad 위치
    keypad = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        0:[3,1]
    }

    # 손이 있어야 할 위치
    left_number = [1,4,7]
    right_number = [3,6,9]
    middle_number = [2,5,8,0]
    
    #손가락 첫 위치
    left_position = [3,0]
    right_position = [3,2]

    # 다음 숫자가 왼쪽, 오른쪽 위치에 있을 때
    for num in numbers:
        if num in left_number:
            result += 'L'
            left_position = keypad[num]
        elif num in right_number:
            result += 'R'
            right_position = keypad[num]

        # 다음 숫자가 가운데 위치에 있을 때
        else:
            # 숫자와 손가락 위치의 거리를 구함
            left_distance = get_distance(keypad, left_position, num)
            right_distance = get_distance(keypad, right_position, num)

            # 오른쪽이 더 가까울 때
            if left_distance > right_distance:
                result += 'R'
                right_position = keypad[num]
            # 왼쪽이 더 가까울 때
            elif left_distance < right_distance:
                result += 'L'
                left_position = keypad[num]

            # 거리가 같을 때 주로 사용하는 손으로 진행
            elif left_distance == right_distance:
                result += hand[0].upper()
                if hand[0] == 'r':
                    right_position = keypad[num]
                elif hand[0] == 'l':
                    left_position = keypad[num]
    return result

"""크레인 인형뽑기 게임"""
def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    bucket = bucket[:-2]
                    answer += 2
                break
    return answer