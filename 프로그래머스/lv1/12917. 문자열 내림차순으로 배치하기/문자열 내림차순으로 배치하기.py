def solution(s):
    answer = ''
    s = [i for i in s]
    s.sort(reverse = True)
    return ''.join(s)