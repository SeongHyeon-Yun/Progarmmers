def solution(X, Y):
    answer = ''
    x_num = {}
    y_num = {}
    
    for j in X:
        x_num[int(j)] = x_num.get(int(j),0)+1
    for j in Y:
        y_num[int(j)] = y_num.get(int(j),0)+1
    
    common_num = list(set(x_num) & set(y_num))
    if len(common_num) == 0 :
        answer = '-1'
    else:
        for key in sorted(common_num,reverse = True):
            num_value = min(x_num[key],y_num[key])

            answer += str(key) * num_value

        if answer[0] == '0':
            answer = '0'
    return answer