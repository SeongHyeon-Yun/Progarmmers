def solution(id_pw, db):
    answer = ''
    user_id, user_pw = id_pw[0], id_pw[1]
    for check_user_id, check_user_pw in db:
        if check_user_id == user_id and check_user_pw == user_pw:
            return 'login'
        
    for check_user_id, check_user_pw in db:
        if check_user_id == user_id and check_user_pw != user_pw:
            return "wrong pw"
        
    for check_user_id, check_user_pw in db:
        if check_user_id != user_id and check_user_pw != user_pw:
            return "fail"
        
    return answer