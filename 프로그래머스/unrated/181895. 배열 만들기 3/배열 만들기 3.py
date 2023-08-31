def solution(arr, intervals):
    answer = []
    num_list = []
    for i in range(len(intervals)):
        num_list.append(arr[intervals[i][0]:intervals[i][1]+1])
    answer = sum(num_list, [])
    return answer