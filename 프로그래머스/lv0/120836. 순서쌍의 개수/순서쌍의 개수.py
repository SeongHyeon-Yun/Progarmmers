def solution(n):
    answer = 0
    result_num = []
    for i in range(1, n +1):
        if n % i == 0:
            j = n // i
            if i * j == n:
                answer += 1
                
    
    return answer