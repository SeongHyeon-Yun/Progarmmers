def solution(n, arr1, arr2):
    answer = []
    arr1 = [bin(i)[2:] for i in arr1]
    arr2 = [bin(i)[2:] for i in arr2]
    
    new_arr1 = []
    new_arr2 = []
    
    for i in arr1:
        if len(i) <= n:
            new_arr1.append('0' * (n - len(i)) + i)
    
    for i in arr2:
        if len(i) <= n:
            new_arr2.append('0' * (n - len(i)) + i)
    
    for i in range(len(new_arr1)):
        result = ''
        for j in range(len(new_arr1)):
            if new_arr1[i][j] == '1' or new_arr2[i][j] == '1':
                result += '#'
            else :
                result += ' '
        answer.append(result)
    return answer