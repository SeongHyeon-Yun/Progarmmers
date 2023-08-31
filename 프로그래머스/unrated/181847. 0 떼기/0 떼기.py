def solution(n_str):
    answer = ''
    count = 0
    while count < len(n_str) and n_str[count] == '0':
        count += 1
        
    answer += n_str[count:]
            
        
    return answer