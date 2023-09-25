def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_dict = {}
    count_num = {}
    for i in id_list:
        report_dict[i] = []
        count_num[i] = 0
    for i in report:
        reporter, ban = i.split(' ')
        report_dict[reporter].append(ban)
        
    for key,value in report_dict.items():
        report_dict[key] = set(value)
    
    for key,value in report_dict.items():
        for i in value:
            count_num[i] += 1
            
    for key,value in count_num.items():
        if value >= k:
            for index,(name,ban) in enumerate(report_dict.items()):
                if key in ban:
                    answer[index] += 1
                
    return answer