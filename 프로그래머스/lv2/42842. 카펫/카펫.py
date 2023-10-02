def solution(brown, yellow):
    answer = []
    sum_num = brown + yellow
    
    for i in range(3,sum_num):
        if sum_num % i == 0:
            w = i
            h = sum_num//i
            if (w-2) * (h-2) == yellow:
                answer = [w,h]
        
    return answer