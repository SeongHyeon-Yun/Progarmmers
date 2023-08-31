def solution(strArr):
    answer = 0
    str_num = {}
    
    for i in strArr:
        length = len(i)
        if length in str_num:
            str_num[length] += 1
        else :
            str_num[length] = 1
    
    answer = max(str_num.values(), default = 0)
    return answer