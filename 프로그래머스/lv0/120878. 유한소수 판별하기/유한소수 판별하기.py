def solution(a, b):
    answer = 1
    factor = []
    denom, numer = a,b
    
    while numer != 0:
        denom, numer = numer, denom % numer
    check_numer = b // denom
    
    num = 2
    
    while check_numer > 1:
        while check_numer % num == 0:
            factor.append(num)
            check_numer //= num
        num += 1
    
    
    factor = list(set(factor))
    
    if 2 in factor:
        factor.remove(2)
    if 5 in factor:
        factor.remove(5)
    
    if len(factor) > 0:
        answer = 2
    
    return answer
