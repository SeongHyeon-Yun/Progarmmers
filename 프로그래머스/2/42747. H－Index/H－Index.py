def solution(citations):
    answer = 0
    
    num_list = []
    
    for i in range(1, len(citations)+1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count < i:
            break
        num_list.append(count)
        
    return len(num_list)