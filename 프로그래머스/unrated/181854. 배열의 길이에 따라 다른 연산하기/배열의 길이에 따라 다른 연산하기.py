def solution(arr, n):
    answer = []  # 수정된 값을 담을 빈 리스트 생성
    
    for index, value in enumerate(arr):
        if len(arr) % 2 == 1 and index % 2 == 0:
            value += n
        elif len(arr) % 2 == 0 and index % 2 == 1:
            value += n
        answer.append(value)  # 수정된 값을 빈 리스트에 추가
    
    return answer