def solution(array, commands):
    answer = []
    for i in commands:
        number = []
        start,end,target = i
        number = array[start-1 : end]
        number.sort()
        answer.append(number[target-1])
        
    return answer