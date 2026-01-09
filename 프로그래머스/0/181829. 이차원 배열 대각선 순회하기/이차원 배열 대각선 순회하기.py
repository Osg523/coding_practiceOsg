def solution(board, k):
    answer = 0
    for i1, j1 in enumerate(board):
        for i2, j2 in enumerate(j1):
            if i1+i2 <= k:
                answer += board[i1][i2]
    return answer