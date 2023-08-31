def solution(numbers):
    answer = [i for i in numbers]
    answer.sort()
    
    return answer[-1] * answer [-2]