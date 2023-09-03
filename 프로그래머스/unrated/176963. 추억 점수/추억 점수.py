def solution(names, yearning, photo):
    answer = []
    score = {}
    for i in range(len(names)):
        score[names[i]] = yearning[i]
    
    for j in photo:
        num = 0
        for k in range(len(j)):
            try :
                num += score[j[k]]
            except:
                num += 0
        answer.append(num)
            
            
    return answer