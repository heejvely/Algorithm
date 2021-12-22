from itertools import combinations

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for i in arr:
        result = sum(i)
        if isPrime(result) == True:
            answer += 1
    return answer