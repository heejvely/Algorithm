def solution(numbers):
    number = list(map(str, numbers))
    number.sort(key = lambda x : x*3,reverse=True)
    return (str(int(''.join(number))))