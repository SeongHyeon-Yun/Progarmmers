def solution(keymap, targets):
    answer = []
    key_list = []
    tuple_list = []
    
    for i in keymap:
        for index, value in enumerate(i):
            key_list.append((index + 1, value))
    
    key_list.sort(key=lambda x: x[0])
    
    for j in key_list:
        if all(j[1] != i[1] for i in tuple_list):
            tuple_list.append(j)
            
    for target in targets:
        count = 0
        for i in target:
            found = False  # 문자열이 tuple_list에 있는지 여부를 나타내는 변수 추가
            for j in tuple_list:
                if i == j[1]:  # 문자열로 비교 수정
                    count += j[0]
                    found = True
                    break
            if not found:
                count = -1
                break
                    
        answer.append(count)
                
    return answer
