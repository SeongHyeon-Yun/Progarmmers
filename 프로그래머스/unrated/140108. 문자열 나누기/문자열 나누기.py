def solution(s):
    result = []  # 분해한 문자열을 저장할 리스트
    
    while s:
        x = s[0]  # 첫 글자를 x로 설정
        count_x = 1
        count_not_x = 0
        
        # 문자열을 왼쪽에서 오른쪽으로 읽으면서 x와 x가 아닌 다른 문자의 개수를 세어줌
        for i in range(1, len(s)):
            if s[i] == x:
                count_x += 1
            else:
                count_not_x += 1
            if count_x == count_not_x:
                break
        
        # 현재까지 읽은 문자열을 분리하고 결과 리스트에 추가
        result.append(s[:count_x + count_not_x])
        s = s[count_x + count_not_x:]
        
    return len(result)

