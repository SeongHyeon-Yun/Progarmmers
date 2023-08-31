def solution(arr):
    answer = 0
    temp_list = arr
    
    while True:
        num_list = []
        for i in temp_list:
            if i >= 50 and i % 2 == 0:
                num_list.append(i // 2)
            elif i < 50 and i % 2 == 1:
                num_list.append(i * 2 + 1)
            else:
                num_list.append(i)
        
        check = all(a==b for a, b in zip(temp_list,num_list))

        if check:
            break
            
        answer += 1
        temp_list = num_list

    return answer