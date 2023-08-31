def solution(myString, pat):
    answer = ''
    end_num = []
    for index, value in enumerate(myString):
        if value in pat:
            end_num.append(index)
    answer = myString[:end_num[-1]+1]
    return answer