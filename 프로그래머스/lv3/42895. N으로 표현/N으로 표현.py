# 이문제는 아직 잘모르겠다


def solution(N, number):
    # 가능한 숫자의 집합을 담는 리스트 초기화
    possible_sets = [set() for _ in range(9)]
    
    # 각 숫자 집합에 숫자 추가
    for i in range(1, 9):
        possible_sets[i].add(int(str(N) * i))
    
    # 연산을 통해 새로운 숫자 추가
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in possible_sets[j]:
                for op2 in possible_sets[i - j]:
                    possible_sets[i].add(op1 + op2)
                    possible_sets[i].add(op1 - op2)
                    possible_sets[i].add(op1 * op2)
                    if op2 != 0:
                        possible_sets[i].add(op1 // op2)
    
    # 목표 숫자가 가능한 숫자 집합에 있는지 확인
    for i in range(1, 9):
        if number in possible_sets[i]:
            return i  # 사용한 숫자의 최소 횟수 반환
    
    return -1  # 불가능한 경우 -1 반환