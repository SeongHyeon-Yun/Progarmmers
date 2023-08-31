def solution(arr):
    answer = []
    arr.reverse()
    while arr:
        answer.append(arr.pop())
        if len(answer) > 1:
            if answer[-1] == answer[-2]:
                del answer[-2]
            
    return answer