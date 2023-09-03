def solution(k, score):
    answer = [score[0]]
    result = []
    for i in range(1,len(score)):
        result.append(answer[0])
        answer.append(score[i])
        answer.sort()
        if len(answer) > k:
            del answer[0]
    result.append(answer[0])
    return result