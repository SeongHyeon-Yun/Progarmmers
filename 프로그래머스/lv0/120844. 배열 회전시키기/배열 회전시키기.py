def solution(numbers, direction):
    answer = []
    if direction == 'right':
        number = numbers.pop()
        numbers.insert(0, number)
        answer = numbers
    else :
        number = numbers.pop(0)
        numbers.append(number)
        answer = numbers
    return answer