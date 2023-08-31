def solution(common):
    answer = []
    start = 0
    end = len(common) - 1
    while start < end:
        start += 1
        answer.append(common[start] - common[start-1])

    if len(set(answer)) == 1:
        return common[-1] + answer[0]
    else:
        return common[-1] * answer[1] // answer[0]
    return answer