def solution(s):
    transform_count = 0
    zero_count = 0
    
    while s != "1":
        # 0 제거
        zero_count += s.count("0")
        s = ''.join([i for i in s if i == '1'])
        
        # 이진 변환
        s = bin(len(s))[2:]
        transform_count += 1
    
    return [transform_count, zero_count]
