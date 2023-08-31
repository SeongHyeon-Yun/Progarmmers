def solution(my_string, is_prefix):
    answer = 0
    str_list=[]
    for i in range(len(my_string)):
        str_list.append(my_string[:i+1])
    for j in str_list:
        if j == is_prefix:
            answer += 1
        else:
            answer += 0
    return answer