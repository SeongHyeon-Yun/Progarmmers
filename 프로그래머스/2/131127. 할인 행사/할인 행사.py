def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        dis_dict = {}
        for j in discount[i:i+10]:
            dis_dict[j] = dis_dict.get(j,0) +1
        
        if dis_dict == want_dict:
            answer += 1
        
    return answer