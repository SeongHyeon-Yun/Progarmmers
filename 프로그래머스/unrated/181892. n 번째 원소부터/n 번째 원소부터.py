def solution(num_list, n):
    answer = []
    for index, value in enumerate(num_list):
        if n-1 == index:
            answer = num_list[index:]
    return answer