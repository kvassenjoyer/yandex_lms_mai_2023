def make_linear(array):
    # "Выпрямление" списка
    result = []
    for element in array:
        if type(element) is list:
            result.extend(make_linear(element))
        else:
            result.append(element)
    return result