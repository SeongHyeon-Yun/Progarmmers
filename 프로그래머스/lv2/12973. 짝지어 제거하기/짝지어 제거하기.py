def solution(s):
    answer = 0
    result = [s[0]]
    
    for i in s[1:]:
        result.append(i)
        if len(result) >= 2 and result[-1] == result[-2]:
            result.pop()
            result.pop()
                
    if len(result) == 0:
        answer = 1

    return answer
