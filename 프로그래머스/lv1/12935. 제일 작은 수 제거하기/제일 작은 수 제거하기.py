def solution(arr):
    
    answer = []
    min_num = min(arr)
    arr.remove(min_num)
    answer = arr
    
    if answer == []:
        answer = [-1]

    return answer