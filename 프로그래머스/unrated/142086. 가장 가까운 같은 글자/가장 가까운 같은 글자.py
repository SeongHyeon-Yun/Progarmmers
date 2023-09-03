def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            answer.append(i - s[:i].rfind(s[i]))
            
    return answer