def solution(score):
    answer = []
    
    for i in score:
        english = i[0]
        math = i[1]
        rank_count = 1
        for j in score:
            if i != j and (english + math) < (j[0] + j[1]):
                rank_count += 1
        answer.append(rank_count)
    return answer