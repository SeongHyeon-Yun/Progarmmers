def solution(arr):
    answer = max(arr)
    
    
    while True:
        for i in arr:
            if answer % i != 0:
                answer += 1
        
        if all(answer % i == 0 for i in arr):
            break
    
    
    return answer