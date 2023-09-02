def solution(strings, n):
    # n번째 문자와 함께 문자열을 저장하는 리스트 생성
    str_list = [(s[n], s) for s in strings]
    
    # 문자열 정렬, 우선순위: n번째 문자, 문자열 자체 (n번째 문자가 같은 경우 사전순으로)
    str_list.sort(key=lambda x: (x[0], x[1]))
    
    # 정렬된 문자열만 추출하여 반환
    answer = [s for _, s in str_list]
    
    return answer