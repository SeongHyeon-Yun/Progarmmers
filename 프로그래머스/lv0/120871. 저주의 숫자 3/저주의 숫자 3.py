def solution(n):
    answer = 1
    start = 1
    num_dict = {i: None for i in range(1, n + 1)}

    while len(num_dict) >= start:
        if answer % 3 != 0 and '3' not in str(answer):
            num_dict[start] = answer
            answer += 1
            start += 1
        else:
            answer += 1

    return num_dict[n]