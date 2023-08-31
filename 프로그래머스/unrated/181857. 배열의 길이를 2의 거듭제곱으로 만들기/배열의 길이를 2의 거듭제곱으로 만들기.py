def solution(arr):
    answer = arr
    exponent = 0
    
    while 2 ** exponent < len(arr):
        exponent += 1
    
    pow_num = 2 ** exponent
    
    if pow_num > len(arr):
        answer += [0] * (pow_num - len(arr))
    
    return answer