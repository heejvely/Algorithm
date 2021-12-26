"""없는 숫자 더하기"""
def solution(numbers):
    num = [i for i in range(10)]
    answer = 0
    for i in num:
        if i not in numbers:
            answer += i
    return answer

"""음양 더하기"""
def solution(absolutes, signs):
    answer = 0
    for idx, i in enumerate(signs):
        if i == True:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
    return answer

"""내적"""
def solution(a,b):
    return sum(list(x*y for x, y in zip(a,b)))

"""소수 만들기"""
from itertools import combinations

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    arr = list(map(sum, combinations(nums,3)))
    answer = 0
    for i in arr:
        if isPrime(i):
            answer += 1
    return answer

"""완주하지 못한 선수"""
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

"""기능 개발"""
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while progresses:
        if (progresses[0]+ speeds[0]*time) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

"""더 맵게(heap)"""
from heapq import *
def solution(scoville,K):
    heapify(scoville)
    count = 0
    while scoville[0] < K and len(scoville) >= 2:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1+ num2*2)
        count +=1
    return count if scoville[0] >= K else -1


"""K번쨰수"""
def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]-1])[i[2]-1]
        answer.append(a)
    return answer