'''
import math

def solution(clothes):
    answer = 0
    clothes_dict = {}
    clothes_num = []
    
    for i in clothes:
        clothes_dict[i[1]] = clothes_dict.get(i[1], 0) + 1
    
    clothes_num = list(clothes_dict.values())
    print(clothes_num)
    if len(clothes_num) == 1:
        answer = clothes_num[0]
        
    elif len(clothes_num) == 2:
        for i in range(len(clothes_num)-1):
            answer += clothes_num[i] * clothes_num[i+1]
        answer += sum(clothes_num)
    
    else:
        answer = 1
        for i in clothes_num:
            answer *= i
            
        for i in range(len(clothes_num)-1):
            answer += clothes_num[i] * clothes_num[i+1]
        answer += clothes_num[0] * clothes_num[-1]
        
        answer += sum(clothes_num)
            
    return answer
'''
from collections import Counter  # collections 모듈로부터 Counter 클래스를 임포트

def solution(clothes):
    # 옷 종류별 개수를 세는 Counter 객체 생성
    clothes_dict = Counter(category for _, category in clothes)
    
    total_combinations = 1  # 초기 값으로 1을 설정
    for count in clothes_dict.values():
        total_combinations *= (count + 1)  # 해당 종류를 입지 않는 경우도 고려해 +1
    
    # 모두 입지 않는 경우를 제외하여 반환
    total_combinations -= 1
    
    return total_combinations  # 가능한 옷 조합의 수를 반환

# 예시 사용법
clothes = [("hat", "head"), ("glasses", "eye"), ("gloves", "hand"), ("shoes", "foot")]
result = solution(clothes)
print(result)  # 출력: 23 (옷을 입는 경우의 수)


