def solution(myString):
    answer = ''
    myString = myString.lower()
    for i in myString:
        if i == 'a':
            i = 'A'
        answer += i
    return answer