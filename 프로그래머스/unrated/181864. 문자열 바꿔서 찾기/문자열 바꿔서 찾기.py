def solution(myString, pat):
    answer = 0
    myString = ['B' if i == 'A' else 'A' for i in myString]
    if pat in ''.join(myString):
        answer += 1
    else :
        answer == 0
    
    return answer