def solution(num, k):
    answer = 0
    num = [i for i in str(num)]
    for index, values in enumerate(num):
        if values == str(k):
            answer = index + 1
            return answer
        else :
            answer = -1

    return answer