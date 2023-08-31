def solution(x):
    answer = True
    num = [int(i) for i in str(x)]
    sum_num = sum(num)
    if x % sum_num != 0:
        answer = False
    
    return answer