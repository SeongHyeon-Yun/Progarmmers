plate = input()
result = [plate[0]]
num = 10
for i in range(1,len(plate)):
    result.append(plate[i])

    if ''.join(result[-2:]) == "()":
        num += 10
    elif ''.join(result[-2:]) == ")(":
        num += 10
    elif ''.join(result[-2:]) == "((":
        num += 5
    else :
        num += 5

print(num)