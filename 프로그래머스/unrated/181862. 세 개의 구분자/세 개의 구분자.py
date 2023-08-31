import re

def solution(myStr):
    answer = re.split('[a-c]', myStr)
    answer = [i for i in answer if i]
    if answer == []:
        answer.append('EMPTY')
    return answer