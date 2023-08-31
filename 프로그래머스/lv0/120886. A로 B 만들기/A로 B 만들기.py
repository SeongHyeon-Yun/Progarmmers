def solution(before, after):
    answer = 0
    str_dict = {}
    
    for i in range(len(before)):
        str_dict[before[i]] = str_dict.get(before[i], 0)+1
        
    for i in range(len(after)):
        str_dict[after[i]] = str_dict.get(after[i], 0)-1
        
    for j in str_dict.values():
        if j == 0:
            answer = 1
        elif j != 0 :
            answer = 0
            break
    return answer