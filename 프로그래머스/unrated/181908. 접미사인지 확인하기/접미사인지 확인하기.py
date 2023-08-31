def solution(my_string, is_suffix):
    answer = 0
    suffix_list=[]
    for i in range(len(my_string)):
        suffix_list.append(my_string[i:])
    for j in suffix_list:
        if is_suffix == j:
            answer += 1
    return answer