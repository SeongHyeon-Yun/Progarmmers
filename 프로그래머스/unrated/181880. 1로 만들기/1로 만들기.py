def solution(num_list):
    answer = 0
    count = 0
    while True:
        for i in range(len(num_list)):
            if num_list[i] % 2 == 0 and num_list[i] > 1:
                num_list[i] = num_list[i] // 2
                answer += 1
            elif num_list[i] % 2 == 1 and num_list[i] > 1:
                num_list[i] -= 1
                num_list[i] = num_list[i] // 2
                answer += 1
        if len(set(num_list)) == 1:
            break
    return answer