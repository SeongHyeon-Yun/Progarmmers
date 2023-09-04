def solution(answers):

    score_1 = [1, 2, 3, 4, 5] * 2000
    score_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    score_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    
    score_people = {'1': 0 ,'2':0, '3':0}
    
    for i in range(len(answers)):
        if answers[i] == score_1[i]:
            score_people['1'] += 1
        if answers[i] == score_2[i]:
            score_people['2'] += 1
        if answers[i] == score_3[i]:
            score_people['3'] += 1    
    
    max_value = max(score_people.values())
    
    answer = [int(key) for key,value in score_people.items() if value == max_value]
    
    return answer