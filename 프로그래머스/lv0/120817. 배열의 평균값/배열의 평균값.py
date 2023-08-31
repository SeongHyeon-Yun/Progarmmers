def solution(numbers):
    number = sum(i for i in numbers)
    answer = number / len(numbers)
    return answer