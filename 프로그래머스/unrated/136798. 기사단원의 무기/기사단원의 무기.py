def solution(number, limit, power):
    answer = 0
    count_list = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            count_list[j] += 1

    for i in range(1, number + 1):
        if count_list[i] > limit:
            answer += power
        else:
            answer += count_list[i]

    return answer

