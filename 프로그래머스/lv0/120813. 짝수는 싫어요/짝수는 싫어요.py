def solution(n):
    answer = [i for i in range(1, n+1)]
    for i in answer:
        if i % 2 == 0:
            answer.remove(i)
    return answer