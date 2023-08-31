def solution(my_string):
    answer = []
    answer_1 = my_string.split(' ')
    for i in answer_1:
        if i == ' ':
            answer_1.pop(' ')
    for j in answer_1:
        if j != '':
            answer.append(j)
    return answer