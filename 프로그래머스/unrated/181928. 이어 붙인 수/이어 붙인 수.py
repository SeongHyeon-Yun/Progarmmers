def solution(num_list):
    answer = 0
    even_num = []
    odd_num = []
    for i in num_list :
        if i % 2 == 0:
            odd_num.append(i)
        elif i % 2 == 1:
            even_num.append(i)
    even_num = list(map(str,even_num))
    odd_num = list(map(str,odd_num))
    answer = int(''.join(even_num)) + int(''.join(odd_num))
    
    return answer