def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    while A:
        a_num = A.pop()
        b_num = B.pop()
        answer += a_num*b_num

    return answer