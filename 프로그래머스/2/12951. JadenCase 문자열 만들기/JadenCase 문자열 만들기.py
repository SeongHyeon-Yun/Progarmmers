def solution(s):
    answer = []
    s = s.lower()
    s = s.split(' ')
    
    for i in s:
        if i == '':
            answer.append('')
        else :
            answer.append(i[0].upper() + i[1:].lower())
            
    return ' '.join(answer)