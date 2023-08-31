def solution(todo_list, finished):
    answer = [todo_list[i] for i, v in enumerate(finished) if v == False]
    
    return answer