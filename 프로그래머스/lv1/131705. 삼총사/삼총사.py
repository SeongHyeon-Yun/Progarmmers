from itertools import combinations as comb

def solution(number):
    answer = 0
    
    for i in comb(number, 3):
        if sum(i) == 0:
            answer += 1
        
    return answer