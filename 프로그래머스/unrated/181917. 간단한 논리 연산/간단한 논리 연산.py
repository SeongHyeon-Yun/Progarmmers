def solution(x1, x2, x3, x4):
    answer = True
    if x1 == False and x2 == False:
        x1_v_x2 = False
    else :
        x1_v_x2 = True
        
    if x3 == False and x4 == False:
        x3_v_x4 = False
    else:
        x3_v_x4 = True
        
    if x1_v_x2 == True and x3_v_x4 == True:
        answer = True
    else:
        answer = False
    
    return answer