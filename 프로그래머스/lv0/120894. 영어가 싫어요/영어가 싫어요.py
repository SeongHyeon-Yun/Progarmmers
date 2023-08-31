def solution(numbers):
    answer = ''
    num_str = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
               "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    piece_str = ''
    for char in numbers:
        piece_str += char
        if piece_str in num_str:
            answer += str(num_str[piece_str])
            piece_str = ''
    return int(answer)