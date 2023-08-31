def solution(hp):
    generals_needed = hp // 5  # 장군개미의 수
    remainder = hp % 5  # 나머지 체력
    
    if remainder == 0:
        return generals_needed
    
    soldiers_needed = remainder // 3  # 병정개미의 수
    remainder %= 3  # 나머지 체력
    
    total_ants_needed = generals_needed + soldiers_needed + remainder
    return total_ants_needed