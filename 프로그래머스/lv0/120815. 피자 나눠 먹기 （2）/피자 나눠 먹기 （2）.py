import math as m

def solution(n):
    
    gcd_num = m.gcd(n, 6)
    lcm_num = n * 6 // gcd_num
    answer = lcm_num // 6
    
    return answer