from itertools import permutations as per

def solution(k, dungeons):
    answer = []
    dungeons = per(dungeons,len(dungeons))
    
    for i in dungeons:
        count = 0
        score = k

        for j in i:
            if score >= j[0]:
                score -= j[1]
                count += 1
            else:
                answer.append(count)
        answer.append(count)
                
    
    return max(answer)