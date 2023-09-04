from itertools import combinations as combi


def solution(nums):
    answer = []
    
    numbers = combi(nums,3)
    for number in numbers:
        prime_num = []
        for i in range(1,sum(number)+1):
            if sum(number) % i == 0:
                prime_num.append(i)
                
        if len(prime_num) == 2:
            answer.append(sum(number))
        
        
    return len(answer)