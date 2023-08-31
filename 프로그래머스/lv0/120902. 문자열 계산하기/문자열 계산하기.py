def solution(my_string):
    
    str_list = my_string.split(' ')
    answer = int(str_list[0])

    for i in range(1, len(str_list), 2):
        if str_list[i] == '+' :
            answer += int(str_list[i+1])
        else :
            answer -= int(str_list[i+1])
    return answer