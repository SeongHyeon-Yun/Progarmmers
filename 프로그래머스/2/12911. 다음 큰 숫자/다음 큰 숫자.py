def solution(n):
    num = 0
    while True:
        one_count = bin(n)[2:].count('1')
        num += 1
        comp_num = n + num
        comp_count = bin(comp_num)[2:].count('1')
        
        if one_count == comp_count:
            return comp_num
        