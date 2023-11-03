import re

def solution(s):
    answer = []
    s = re.findall(r'\d+', s)
    num_dict = {}
    
    for i in s:
        num_dict[i] = num_dict.get(i,0) + 1
    
    num_dict = sorted(num_dict.items(), key= lambda x:x[1], reverse = True)
    
    for i in num_dict:
        answer.append(int(i[0]))
    return answer