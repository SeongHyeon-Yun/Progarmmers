def solution(cacheSize, cities):
    answer = 0
    cache_list = []
    cities = [i.lower() for i in cities]
    
    for citi in cities:
        if citi not in cache_list:
            if len(cache_list) < cacheSize:
                cache_list.append(citi)
                answer += 5
            else:
                cache_list.append(citi)
                cache_list.pop(0)
                answer += 5
        else:
            cache_list.remove(citi)
            cache_list.append(citi)
            answer += 1

    return answer