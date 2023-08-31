from math import comb as c

def solution(balls, share):
    answer = c(balls, share)
    return answer