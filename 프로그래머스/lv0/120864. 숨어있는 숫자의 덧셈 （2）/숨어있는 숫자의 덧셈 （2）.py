def solution(my_string):
    num_list = []
    piece_num = ''
    
    for i in my_string:
        try:
            int_value = int(i)
            piece_num += i
        except ValueError:
            if piece_num:
                num_list.append(piece_num)
                piece_num = ''
    
    if piece_num:  # 마지막 숫자 조각이 있는지 확인
        num_list.append(piece_num)
    
    num_list = [int(i) for i in num_list]
    
    return sum(num_list)
