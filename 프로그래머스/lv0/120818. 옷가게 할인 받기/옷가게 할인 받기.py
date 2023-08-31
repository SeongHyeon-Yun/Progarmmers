def solution(price):

    if price >= 500000:
        discount = 0.8
    elif price >= 300000:
        discount = 0.9
    elif price >= 100000:
        discount = 0.95
    else :
        discount = 1
        
    answer = price * discount
    return int(answer)