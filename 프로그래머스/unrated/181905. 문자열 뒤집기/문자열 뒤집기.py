def solution(my_string, s, e):
    answer = ''
    my_list = list(my_string)
    my_list[s:e+1] = reversed(my_list[s:e+1])
    answer = ''.join(my_list)    
    return answer