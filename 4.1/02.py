def gcd(a, b):
    # Функциональный НОД

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a
