import numpy as np


def multiplication_matrix(N):
    # Матрица умножения

    line = np.arange(1, N + 1)
    return np.multiply(line.reshape(N, 1), line)
