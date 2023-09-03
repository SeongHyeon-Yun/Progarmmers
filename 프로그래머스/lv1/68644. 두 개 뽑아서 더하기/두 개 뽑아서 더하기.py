from itertools import combinations as com

def solution(numbers):
    answer = []
    for i in com(numbers,2):
        if sum(i) not in answer:
            answer.append(sum(i))
            
    answer.sort()
    
    return answer