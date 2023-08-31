def solution(dots):
    answer = 0
    x = [dots[i][0] for i in range(len(dots))]
    y = [dots[i][1] for i in range(len(dots))]
    
    answer = (max(x) - min(x)) *(max(y) - min(y))
    return answer