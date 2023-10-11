def solution(N, stages):
    result = {}
    stages.sort()
    total_players = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        if total_players == 0:
            result[i] = 0
        else:
            result[i] = count / total_players
        total_players -= count
    
    result = [key for key, value in sorted(result.items(), reverse=True, key=lambda x: x[1])]
    return result