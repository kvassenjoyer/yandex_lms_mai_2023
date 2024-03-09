import numpy as np


def make_board(N):
    # Шахматная подготовка

    board = np.ones((N, N), dtype="int8")
    for i in range(N):
        for j in range(N):
            board[i][j] -= (i + j) % 2
    return board
