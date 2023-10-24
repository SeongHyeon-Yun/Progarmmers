def solution(numbers):
    answer = [i for i in range(10)]
    
    return sum(set(answer) - set(numbers))