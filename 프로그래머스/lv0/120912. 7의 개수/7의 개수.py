def solution(array):
    answer = 0
    array = [str(i) for i in array]
    
    for i in array:
        for j in i:
            if j == '7':
                answer += 1
    return answer