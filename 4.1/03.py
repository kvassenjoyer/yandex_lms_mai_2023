def number_length(number):
    # Длина числа

    if number < 0:
        number *= -1

    return len(str(number))
