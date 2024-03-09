import numpy as np


def stairs(array):
    # Лесенка

    N = array.shape[0]

    matrix = np.zeros((N, N), dtype="int8")
    for i in range(N):
        for j in range(N):
            matrix[i][(j + i) % N] = array[j]

    return matrix
