def solution(lines):
    answer = 0
    check_num = {}
    for line in lines:
        for i in range(line[0], line[1]):
            check_num[i] = check_num.get(i,0)+1
        
    num = {key for key, value in check_num.items() if value > 1}
    
    
    return len(num)