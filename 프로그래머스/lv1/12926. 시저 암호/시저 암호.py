def solution(s, n):
    answer = ''

    for i in s:
        if 'A' <= i <= 'Z':
            # 대문자 처리
            new_char = chr(((ord(i) - ord('A') + n) % 26) + ord('A'))
            answer += new_char
        elif 'a' <= i <= 'z':
            # 소문자 처리
            new_char = chr(((ord(i) - ord('a') + n) % 26) + ord('a'))
            answer += new_char
        else:
            # 알파벳이 아닌 문자는 그대로 추가
            answer += i

    return answer