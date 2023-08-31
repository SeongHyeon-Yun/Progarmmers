def solution(dots):
    answer = 0
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    
    slope_12 = (y2 - y1) / (x2 - x1)
    slope_34 = (y4 - y3) / (x4 - x3)
    slope_23 = (y3 - y2) / (x3 - x2)
    slope_14 = (y4 - y1) / (x4 - x1)
    
    if slope_12 == slope_34 or slope_23 == slope_14:
        answer = 1
    else:
        answer = 0
        
    return answer