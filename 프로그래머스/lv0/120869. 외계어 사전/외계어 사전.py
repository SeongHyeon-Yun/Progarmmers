def solution(spell, dic):
    answer = 0
    str_dict = {}
    
    for i in spell:
        str_dict[i] = str_dict.get(i, 0) + 1
        
    for j in dic:
        temp_dict = str_dict.copy()
        for k in j:
            if k in temp_dict:
                temp_dict[k] -= 1
        
        if all(value == 0 for value in temp_dict.values()):
            answer = 1
            break
            
    if answer == 0:
        answer = 2
        
    return answer