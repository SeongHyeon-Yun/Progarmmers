def solution(sides):
    answer = []
    c = 1
    a,b = sides
    while c < 2000:
        if a + b > c and a + c > b and b + c > a:
            answer.append(c)

        c += 1
        
    return len(answer)