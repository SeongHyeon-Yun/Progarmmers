def solution(my_string):
    answer = ''
    string = 'aeiou'
    for i in my_string:
        if i not in string:
            answer += i
                
    return answer