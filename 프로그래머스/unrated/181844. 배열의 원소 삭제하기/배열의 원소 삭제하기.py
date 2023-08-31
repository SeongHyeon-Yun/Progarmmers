def solution(arr, delete_list):
    answer = []
    common = set(arr) & set(delete_list)
    
    for i in arr:
        if i not in common:
            answer.append(i)
    return answer