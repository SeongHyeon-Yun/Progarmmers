def solution(s):
    picture = []  # 괄호 문자열을 저장할 스택
    
    for char in s:
        if char == '(':
            picture.append(char)
        elif char == ')':
            if not picture:  # 스택이 비어있으면 올바르지 않은 괄호 문자열
                return False
            picture.pop()  # 스택에서 열린 괄호를 제거
    
    return len(picture) == 0  # 스택이 비어 있으면 올바른 괄호 문자열
