def solution(str1, str2):
    answer = 0
    str1_list, str2_list = [], []
    
    for i in range(len(str1)-1):
        temp = str1[i]+str1[i+1]
        if temp.isalpha():
            str1_list.append(temp.lower())
            
    for i in range(len(str2)-1):
        temp = str2[i]+str2[i+1]
        if temp.isalpha():
            str2_list.append(temp.lower())
            
    temp = str1_list.copy()
    sum_list = str1_list.copy()
    common_list = []
    
    for i in str2_list:
        if i in temp:
            temp.remove(i)
        else:
            sum_list.append(i)
            
    for i in str1_list:
        if i in str2_list:
            common_list.append(i)
            str2_list.remove(i)
    
    if len(sum_list) != 0 and common_list != 0:
        answer = int((len(common_list)/len(sum_list)) * 65536)
    else:
        answer = 1*65536
        
        
    return answer