def same_type(input_func):
    # Однотипность не порок
    def wrapper(*args):
        typename = type(args[0])
        for arg in args:
            if type(arg) is not typename:
                print("Обнаружены различные типы данных")
                break
        else:
            return input_func(*args)

    return wrapper
