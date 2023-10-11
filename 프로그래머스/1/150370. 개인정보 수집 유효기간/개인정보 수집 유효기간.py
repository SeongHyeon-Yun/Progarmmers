def solution(today, terms, privacies):
    answer = []
    year, month, day = today.split('.')
    terms_dict = {}
    today_cal = [int(year),int(month),int(day)]
    
    for i in terms:
        terms_dict[i[0]] = int(i[2:])
    
    for index, value in enumerate(privacies):
        cal_list = []
        calender, term = value.split(' ')
        cal_y, cal_m, cal_d = calender.split('.')
        cal_y, cal_m, cal_d = int(cal_y), int(cal_m), int(cal_d)
        cal_m += terms_dict[term]
        
        
        if cal_m > 12:
            if cal_m % 12 == 0:
                cal_y = cal_y + (cal_m // 12)-1
                cal_m = 12

            else:
                cal_y = cal_y + (cal_m // 12)
                cal_m = cal_m % 12
            
        if cal_d - 1 == 0:
            cal_d = 28
            cal_m -= 1
            if cal_m == 0:
                cal_m = 12
                cal_y -= 1
        else :
            cal_d -= 1
            
        cal_list = [cal_y,cal_m,cal_d]
        
        if cal_list < today_cal:
            answer.append(index+1)
            
            
            
    return answer