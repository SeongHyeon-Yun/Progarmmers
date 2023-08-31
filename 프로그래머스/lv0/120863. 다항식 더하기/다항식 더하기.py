def solution(polynomial):
    answer = ''
    terms = polynomial.replace(' ', '').split('+')

    x_sum = 0
    num_sum = 0

    for term in terms:
        if 'x' in term:
            if len(term) > 1:
                x_sum += int(term[:-1])
            else:
                x_sum += 1
        else:
            num_sum += int(term)

    if x_sum == 0:
        answer += str(num_sum)
    elif num_sum == 0:
        if x_sum == 1:
            answer += 'x'
        else:
            answer += f'{x_sum}x'
    else:
        if x_sum == 1:
            answer += f'x + {num_sum}'
        else:
            answer += f'{x_sum}x + {num_sum}'

    return answer