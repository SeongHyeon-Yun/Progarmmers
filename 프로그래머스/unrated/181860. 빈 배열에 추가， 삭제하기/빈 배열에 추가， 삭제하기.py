def solution(arr, flag):
    answer = []
    count = 0
    for i in flag:
        if i == True:
            for j in range(arr[count] * 2):
                answer.append(arr[count])
        else :
            for k in range(arr[count]):
                answer.pop(-1)
        count += 1
    return answer