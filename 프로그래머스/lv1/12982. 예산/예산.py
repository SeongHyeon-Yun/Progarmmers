def solution(d, budget):
    answer = 0
    d.sort()

    if sum(d) <= budget:
        return len(d)
    elif sum(d) > budget:
        for index, value in enumerate(d):
            budget = budget - value
            if budget < 0:
                return len(d[:index])