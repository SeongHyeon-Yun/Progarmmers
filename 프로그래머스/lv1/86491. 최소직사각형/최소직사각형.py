def solution(sizes):
    max_width = 0
    max_height = 0
    
    for i in sizes:
        width, height = i
        max_width = max(max_width, max(width, height))
        max_height = max(max_height, min(width, height))
    
    wallet_size = max_width * max_height
    return wallet_size