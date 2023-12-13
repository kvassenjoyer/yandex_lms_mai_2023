def fibonacci(n):
    # Генератор Фибоначчи
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
