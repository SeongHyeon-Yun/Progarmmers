def solution(n, m):
    answer = []
    gcd, b = m, n
    while b > 0:
        gcd,b = b, gcd%b
        
    answer = [gcd, n * m // gcd]
    return answer