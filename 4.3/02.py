def recursive_digit_sum(number):
    # Рекурсивный сумматор цифр
    if number < 10:
        return number
    else:
        return number % 10 + recursive_digit_sum(number // 10)
