def solution(numLog):
    answer = ''
    num1 = []
    num2 = []
    for i in range(0,len(numLog)-1):
        num1.append(numLog[i])
    for j in range(1,len(numLog)):
        num2.append(numLog[j])
    for k in range(len(num1)):
        if -(num1[k]-num2[k]) == 1:
            answer += 'w'
        elif -(num1[k]-num2[k]) == -1:
            answer += 's'
        elif -(num1[k]-num2[k]) == 10:
            answer += 'd'
        elif -(num1[k]-num2[k]) == -10:
            answer += 'a'

    return answer