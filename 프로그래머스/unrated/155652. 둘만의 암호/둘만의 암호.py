def solution(s, skip, index):
    answer = ''
    s = [ord(i) for i in s]
    skip = [ord(i) for i in skip]
    
    for i in range(len(s)):
        count = 0
        while count < index:
            s[i] += 1
            if s[i] > 122:
                s[i] = 97
            if s[i] not in skip:
                count += 1
        answer += chr(s[i])

    return answer
