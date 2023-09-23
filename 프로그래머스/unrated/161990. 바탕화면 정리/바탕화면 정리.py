def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = [],[],[],[]
    for i,v in enumerate(wallpaper):
        if '#' in v:
            lux.append(i)
        for index, value in enumerate(v):
            if value == '#':
                luy.append(index)
    answer = [min(lux),min(luy),max(lux)+1,max(luy)+1]
    
    return answer