def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

def solution(prices):
    length = len(prices)
    answer = [i for i in range(length -1, -1, -1)]

    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i -j
        stack.append(i)
    return answer