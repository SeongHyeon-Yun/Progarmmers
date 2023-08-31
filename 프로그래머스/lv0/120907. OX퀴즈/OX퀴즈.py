def solution(quiz):
    answer = []
    quiz = [i.split(' ') for i in quiz]

    for i in quiz:
        if i[1] == '-':
            result = int(i[0]) - int(i[2])
            if result == int(i[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            result = int(i[0]) + int(i[2])
            
            if result == int(i[4]):
                answer.append('O')
            else:
                answer.append('X')
                
    return answer