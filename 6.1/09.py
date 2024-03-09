import numpy as np


def rotate(matrix, angle):
    # Вращение
    
    return np.rot90(matrix, k=4 - angle // 90)
