def only_positive_even_sum(a, b):
    # Контроль параметров

    if any(map(lambda x: not isinstance(x, int), [a, b])):
        raise TypeError
    elif any(map(lambda x: x <= 0 or x % 2 == 1, [a, b])):
        raise ValueError
    else:
        return a + b
