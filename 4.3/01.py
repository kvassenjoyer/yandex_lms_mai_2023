def recursive_sum(*args):
    # Рекурсивный сумматор
    if args:
        return args[0] + recursive_sum(*args[1:])
    else:
        return 0
