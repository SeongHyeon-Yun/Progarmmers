def solution(numbers, k):
    answer = numbers*k
    answer = answer[::2]
    
    
    return answer[k-1]