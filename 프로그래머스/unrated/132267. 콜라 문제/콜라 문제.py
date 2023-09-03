def solution(a, b, n):
    answer = 0
    
    while n >= a:
        
        empty_bottle = (n // a) * a
        bottle = (empty_bottle // a) * b
        n = n - empty_bottle + bottle
        answer += bottle
        
    return answer