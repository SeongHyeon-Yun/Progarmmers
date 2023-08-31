def solution(num_list):
    answer = 0
    num = 0
    num2 = 1
    result_list = []
    
    for i in num_list:
        num += i
    num *= num
    result_list.append(num)

    for j in num_list:
        num2 *= j
    result_list.append(num2)
    
    if result_list[0] > result_list[1]:
        answer = 1
    else :
        answer = 0
    
    return answer