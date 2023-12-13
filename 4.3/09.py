def cycle(array):
    # Циклический генератор
    while True:
        yield from array
