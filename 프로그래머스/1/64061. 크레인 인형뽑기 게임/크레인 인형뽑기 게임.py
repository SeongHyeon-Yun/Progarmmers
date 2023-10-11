def solution(board, moves):
    answer = 0
    select_num = []
    while len(moves) > 0:
        target = moves.pop(0)
        for i in board:
            if i[target-1] != 0:
                select_num.append(i[target-1])
                i[target-1] = 0
                break
        if len(select_num) >= 2:
            if select_num[-1] == select_num[-2]:
                del select_num[-2:]
                answer += 2
    return answer