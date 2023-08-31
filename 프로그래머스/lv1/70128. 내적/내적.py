def solution(a, b):
    answer = 0
    count = 0
    
    while count != len(a):
        answer += a[count] * b[count]
        count += 1
    return answer