def solution(array, n):
    answer = 0
    result = {}
    array.sort()
    
    for i in range(len(array)):
        result[i] = abs(array[i] - n)
    min_index = min(result.items(), key=lambda item : item[1])[0]
    
    return array[min_index]