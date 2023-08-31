def solution(emergency):
    answer = [i for i in emergency]
    answer_2 = []
    result = {}
    emergency.sort(reverse = True)
    for i in range(len(emergency)):
        result[emergency[i]] = result.get(emergency[i], i + 1)
    for j in answer:
        answer_2.append(result[j])
    return answer_2