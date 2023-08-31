def solution(n):
    answer = 1
    
    while True:
        num = n % answer
        if num != 1:
            answer += 1
        elif num == 1:
            return answer
    return answer