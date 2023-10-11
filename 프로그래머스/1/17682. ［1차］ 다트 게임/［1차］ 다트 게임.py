import re

def solution(dartResult):
    darts = re.findall('([0-9]+)([SDT])([*#]?)',dartResult)
    answer = [0] * len(darts)
    
    for index,(num, square, option) in enumerate(darts):
        answer[index] = int(num)
        if square == 'D':
            answer[index] = int(num) ** 2
        elif square == 'T':
            answer[index] = int(num) ** 3
            
        if option == '*':
            answer[index] *= 2
            if 0 <= index - 1:
                answer[index - 1] *= 2
        elif option == '#':
            answer[index] *= -1
            
    return sum(answer)