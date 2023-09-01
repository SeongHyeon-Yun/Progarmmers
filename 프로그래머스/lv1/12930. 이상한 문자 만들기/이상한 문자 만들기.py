def solution(s):
    answer = ''
    s = [i for i in s]
    s.reverse()
    count = 0
    
    while s:
        r = s.pop()
        if count % 2 == 0:
            r = r.upper()
        else :
            r = r.lower()
        count += 1
        answer += r
        if r == ' ':
            count = 0
    return answer