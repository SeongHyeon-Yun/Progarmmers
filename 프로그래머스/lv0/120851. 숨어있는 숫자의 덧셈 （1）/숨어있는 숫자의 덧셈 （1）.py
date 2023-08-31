def solution(my_string):
    answer = 0
    for i in my_string:
        if 47 < ord(i) < 58:
            answer += int(i)
    return answer