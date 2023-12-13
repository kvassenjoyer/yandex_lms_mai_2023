def make_matrix(size, value=0):
    # Генератор матриц

    if type(size) is int:
        matrix_height = size
        matrix_width = size
    elif len(size) == 2:
        matrix_height = size[1]
        matrix_width = size[0]

    result_matrix = []
    for _ in range(matrix_height):
        matrix_line = []
        for _ in range(matrix_width):
            matrix_line.append(value)
        result_matrix.append(matrix_line)

    return result_matrix
