def solution(n):
    answer = []
    num = 2
    while n > 1:
        while n % num == 0:
            answer.append(num)
            n = n // num
        num += 1
    answer = list(set(answer))
    answer.sort()
    return answer