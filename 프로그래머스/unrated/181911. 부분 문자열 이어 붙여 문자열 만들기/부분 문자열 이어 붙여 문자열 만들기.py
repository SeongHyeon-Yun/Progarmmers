def solution(my_strings, parts):
    answer = ''
    my_list = []
    for i in range(len(my_strings)):
        my_list.append(my_strings[i][parts[i][0]:parts[i][1]+1])
    answer = ''.join(my_list)
    return answer