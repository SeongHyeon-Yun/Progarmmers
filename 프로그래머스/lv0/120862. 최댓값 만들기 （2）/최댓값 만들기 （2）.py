def solution(numbers):
    answer = 0
    numbers.sort()
    max_num = [numbers[0] * numbers[1], numbers[-1] * numbers[-2]]
    answer = max(max_num)
    return answer