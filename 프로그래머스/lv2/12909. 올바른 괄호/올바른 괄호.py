def solution(s):
    stack = []  # 스택을 사용하여 괄호 짝을 검사할 리스트

    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not stack:  # 스택이 비어있으면 올바르지 않은 괄호 문자열
                return False
            stack.pop()  # 스택에서 열린 괄호를 제거

    return len(stack) == 0  # 스택이 비어 있으면 올바른 괄호 문자열
