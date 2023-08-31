def solution(a, d, included):
    answer = 0
    list_i = []
    num = 0
    for i in range(len(included)):
        answer = a + d
        a = answer
        answer -= d
        list_i.append(answer)
        
        if included[i] == True:
            num += list_i[i]
    
    answer = num
    
    return answer