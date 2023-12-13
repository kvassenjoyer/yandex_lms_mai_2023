def answer(input_func):
    # Декор результата
    def wrapper(*args, **kwargs):
        return f"Результат функции: {input_func(*args, **kwargs)}"

    return wrapper
