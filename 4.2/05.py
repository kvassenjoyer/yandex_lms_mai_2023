def to_string(*args, sep=" ", end="\n"):
    # Подготовка данных

    result_string = ""
    for i in range(len(args)):
        if i == len(args) - 1:
            result_string += str(args[i]) + end
        else:
            result_string += str(args[i]) + sep
    return result_string
