import numpy as np

def solution(board):
    board = np.array(board)
    n = len(board)
    origin = board.copy()
    for j, board1 in enumerate(origin): 
        for i, board2 in enumerate(board1):
            if board2 == 1:
                col_start = 0 if i == 0 else i - 1
                col_end = i + 2
                if j == 0:
                    board[j:j+2, col_start:col_end] = 1
                elif j > 0 and j < n - 1: 
                    board[j-1:j+2, col_start:col_end] = 1
                elif j == n - 1:
                    board[j-1:j+1, col_start:col_end] = 1
    return int(np.count_nonzero(board == 0))