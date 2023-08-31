def solution(sides):
    answer = 0
    max_num = max(sides)
    if sum(sides) - max_num > max_num:
        answer = 1
    else :
        answer = 2
    return answer