def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:  # 조건 수정
                answer += board[i][j]  # board[i][j]를 더하도록 수정

    return answer