def solution(myString):
    answer = myString.split('x')
    answer.sort()
    answer = [i for i in answer if i]
    return answer