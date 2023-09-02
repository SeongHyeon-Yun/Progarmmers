def solution(s):
    answer = ''
    num_str = ''
    num_eng = {'zero':0 ,'one':1 ,'two':2 ,'three':3 ,'four':4 ,'five':5
              ,'six':6 ,'seven':7 ,'eight':8 ,'nine':9}
    
    for i in s:
        if i.isdigit():
            answer += i
        else:
            num_str += i
            if num_str in num_eng: 
                answer += str(num_eng[num_str]) 
                num_str = '' 
    
    return int(answer)