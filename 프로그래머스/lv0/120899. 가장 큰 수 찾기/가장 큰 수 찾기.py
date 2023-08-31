def solution(array):
    
    max_num = max(array)
    index_num = array.index(max_num)
    answer = [max_num, index_num]
    return answer