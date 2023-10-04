def solution(arr):
    answer = max(arr)
    
    
    while True:

        
        if all(answer % i == 0 for i in arr):
            break
        else:
            answer += 1
    
    return answer