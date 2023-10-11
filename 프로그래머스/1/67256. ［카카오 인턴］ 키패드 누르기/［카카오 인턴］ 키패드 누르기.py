def solution(numbers, hand):
    answer = ''
    keypads = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        0:(3,1)
    }
    left, right = (3,0),(3,2)
    
    for i in numbers:
        if i in [1,4,7]:
            left = keypads[i]
            answer += 'L'
        elif i in [3,6,9]:
            right = keypads[i]
            answer += 'R'
        else :
            l_num = abs(left[0] - keypads[i][0]) + abs(left[1] - keypads[i][1])
            r_num = abs(right[0] - keypads[i][0]) + abs(right[1] - keypads[i][1])
            
            if l_num > r_num:
                answer += 'R'
                right = keypads[i]
                
            elif l_num < r_num:
                answer += 'L'
                left = keypads[i]
                
            else :
                answer += hand[0].upper()
                
                if hand[0].upper() =='L':
                    left = keypads[i]
                else:
                    right = keypads[i]
            
    return answer