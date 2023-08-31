def solution(s):
    answer = ''
    str_num = {}
    
    for i in s:
        str_num[i] = str_num.get(i, 0) +1

    for index, value in sorted(str_num.items()):
        if value == 1:
            answer += index
    return answer