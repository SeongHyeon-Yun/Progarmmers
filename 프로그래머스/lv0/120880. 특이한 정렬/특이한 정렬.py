def solution(numlist, n):
    answer = []
    num_dict = {}
    for i in numlist:
        num_dict[i] = num_dict.get(i, abs(n-i))
    num_dict = sorted(num_dict.items(), key=lambda x:(x[1], -x[0]))
    for i in num_dict:
        answer.append(i[0])
    return answer