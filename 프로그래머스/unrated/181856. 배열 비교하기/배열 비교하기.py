def solution(arr1, arr2):
    answer = 0
    a = sum(arr1)
    b = sum(arr2)
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        if a > b:
            answer = 1
        elif a < b:
            answer = -1
        else :
            answer = 0
    return answer
