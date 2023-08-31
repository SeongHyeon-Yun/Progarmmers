def solution(babbling):
    answer = 0
    
    for i in babbling:
        while True:
            if i[:3] in ["aya","woo"]:
                i = i[3:]
            elif i[:2] in ["ye", "ma"]:
                i = i[2:]
            else:
                break

        if i == "":
            answer += 1
    return answer