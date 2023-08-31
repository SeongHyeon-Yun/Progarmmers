def solution(number):
    answer = 0
    sum_number = 0
    for i in range(len(number)):
        sum_number += int(number[i])
    answer = sum_number % 9
    return answer