import itertools


def rabbit(start, finish, length):
    # Путешествие кролика

    result = []
    for jumps in itertools.product([-2, -1, 1, 2], repeat=length):
        if sum(jumps) == finish - start:
            jumps_history = []

            position = start
            for jump_lenght in jumps:
                position += jump_lenght
                jumps_history.append(position)

            if start not in jumps_history and len(set(jumps_history)) == length:
                result.append([start] + jumps_history)

    return result
