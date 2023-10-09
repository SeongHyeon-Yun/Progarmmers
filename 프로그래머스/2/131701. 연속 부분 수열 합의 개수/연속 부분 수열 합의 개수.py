def solution(elements):
    
    answer = []
    num_list = elements * 2
    
    for j in range(1,len(elements)+1):
        for i in range(len(num_list)):
            answer.append(sum(num_list[i:i+j]))
            
    return len(set(answer))