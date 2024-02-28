def merge(a, b):
    # Слияние с проверкой

    if not hasattr(a, "__iter__") or not hasattr(b, "__iter__"):
        raise StopIteration

    c = list(a) + list(b)
    if not all(isinstance(x, type(a[0])) for x in c):
        raise TypeError

    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError

    return tuple(sorted(c))
