def solution(survey, choices):
    answer = ''
    personality = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    personality_tuple = []
    for i in range(len(survey)):
        if 1 <= choices[i] <= 3:
            personality[survey[i][0]] += abs(choices[i] - 4)
        elif 4 <= choices[i] <= 7:
            personality[survey[i][1]] += abs(choices[i] - 4)
            
    for index, (key,value) in enumerate(personality.items()):
        personality_tuple.append((key, value))
    
    for i in range(1,len(personality_tuple),2):
        if personality_tuple[i-1][1] > personality_tuple[i][1]:
            answer += personality_tuple[i-1][0]
        elif personality_tuple[i-1][1] < personality_tuple[i][1]:
            answer += personality_tuple[i][0]
        
        if personality_tuple[i-1][1] == personality_tuple[i][1]:
            answer += personality_tuple[i-1][0]
            
        print(personality_tuple[i-1], personality_tuple[i])
    return answer