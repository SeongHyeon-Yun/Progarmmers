def solution(lottos, win_nums):
    min_num = len(set(lottos) & set(win_nums))
    max_num = len(set(lottos) & set(win_nums)) + lottos.count(0)
    answer = [max_num, min_num]
    
    for i in range(len(answer)):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else :
            answer[i] = 6

    return answer