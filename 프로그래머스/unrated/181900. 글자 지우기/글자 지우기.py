def solution(my_string, indices):
    answer = ''
    str_list = list(my_string)
    for i in indices:
        str_list[i] = 0
    while 0 in str_list:
        str_list.remove(0)
    answer = ''.join(str_list)
    return answer