def solution(array):
    freq_dict = {}  # 각 숫자의 빈도수를 저장할 딕셔너리
    
    for num in array:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_freq = max(freq_dict.values())  # 가장 높은 빈도수 찾기
    
    mode = -1  # 최빈값 초기화
    multiple_modes = False  # 여러 개의 최빈값을 판단하기 위한 변수
    
    for num, freq in freq_dict.items():
        if freq == max_freq:
            if mode == -1:  # 최빈값이 처음 나온 경우
                mode = num
            else:  # 이미 최빈값이 있으면 여러 개의 최빈값이 존재하는 것으로 판단
                multiple_modes = True
                break
    
    if multiple_modes:
        return -1
    else:
        return mode