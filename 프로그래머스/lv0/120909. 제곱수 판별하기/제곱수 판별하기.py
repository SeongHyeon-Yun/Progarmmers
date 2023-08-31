def solution(n):
    answer = 0
    num = 0
    for i in range(n//2):
        if i**2 == n:
            answer = 1
            return answer
        
        else:
            answer = 2
    
    return answer