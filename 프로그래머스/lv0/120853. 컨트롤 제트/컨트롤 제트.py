def solution(s):
    num = []
    s = s.split(' ')
    for i in s:
        num.append(i)
        if i == 'Z':
            num.pop()
            num.pop(-1)
    if len(num) == 0:
        answer = 0
    
    answer = list(map(int, num))
    return sum(answer)