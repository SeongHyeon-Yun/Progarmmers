def solution(participant, completion):
    answer= ''
    n = {}
    for i in participant:
        n[i] = n.get(i, 0) + 1
    for j in completion:
        n[j] -= 1
    answer = ''.join([k for k, v in n.items() if v == 1])
    return answer