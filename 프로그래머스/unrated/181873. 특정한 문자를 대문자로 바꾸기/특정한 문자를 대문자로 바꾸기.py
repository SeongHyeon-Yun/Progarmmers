def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        answer = my_string.replace(alp, alp.upper())
    else:
        answer = my_string
    return answer