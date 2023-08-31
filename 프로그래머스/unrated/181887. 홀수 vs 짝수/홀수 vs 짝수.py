def solution(num_list):
    even_num = [v for i, v in enumerate(num_list) if i % 2 == 0]
    odd_num = [v for i, v in enumerate(num_list) if i % 2 ==1]

    return max(sum(even_num),sum(odd_num))