def solution(ingredient):
    answer = []
    count = 0
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1,2,3,1]:
            count += 1
            del answer[-4:]
            
            
    
    
    return count