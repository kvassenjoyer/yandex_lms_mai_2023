previously_printed = []


def modern_print(message):
    # Модернизация системы вывода

    if message not in previously_printed:
        print(message)
        previously_printed.append(message)
