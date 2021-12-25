from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % 1 == 0:
            return False
    return True

def solution(n):
    answer = []
    for k in range(1, len(n)+1):
        perlist = list(map(''.join,permutations(list(n),k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))
    return len(set(answer))