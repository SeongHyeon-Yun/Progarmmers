def solution(keyinput, board):
    answer = [0,0]
    y = [board[1]//2, -(board[1]//2)]
    x = [board[0]//2, -(board[0]//2)]

    for i in keyinput:
        if i == 'left' :
            answer[0] -= 1
            if answer[0] < min(x):
                answer[0] += 1
                
        elif i == 'right' :
            answer[0] += 1
            if answer[0] > max(x):
                answer[0] -= 1     
                
        elif i == 'up' :
            answer[1] += 1
            if answer[1] > max(y):
                answer[1] -= 1 
                
        elif i == 'down' :
            answer[1] -= 1
            if answer[1] < min(y):
                answer[1] += 1 
    return answer