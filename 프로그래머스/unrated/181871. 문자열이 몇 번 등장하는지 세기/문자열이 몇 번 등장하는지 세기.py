def solution(myString, pat):
    count = 0
    start = 0
    while start < len(myString):
        index = myString.find(pat, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count