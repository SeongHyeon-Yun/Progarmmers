def solution(food):
    answer = ''
    reverse_str = ''
    for index, value in enumerate(food):
        answer += str(index) * (value // 2)
    
    for i in answer:
        reverse_str = i + reverse_str
            
    
    answer = answer+ '0' +reverse_str
    
    return answer