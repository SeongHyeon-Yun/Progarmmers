def solution(my_string, num1, num2):
    answer = ''
    my_string = [i for i in my_string]
    piece1 = my_string.pop(num1)
    piece2 = my_string.pop(num2 - 1)

    my_string.insert(num1, piece2)
    my_string.insert(num2, piece1)
    answer = ''.join(my_string)
    return answer