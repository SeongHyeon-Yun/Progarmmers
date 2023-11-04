import math

def solution(progresses, speeds):
    answer = []
    dead_line = []
    count = 0
    
    for i in range(len(progresses)):
        prog_day = math.ceil((100 - progresses[i]) / speeds[i])
        dead_line.append(prog_day)

    num = dead_line[0]
    count = 1
    
    for i in range(1, len(dead_line)):
        if num >= dead_line[i]:
            count += 1
        else:
            num = dead_line[i]
            answer.append(count)
            count = 1
        
    answer.append(count)

        
    return answer