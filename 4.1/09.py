def is_prime(number):
    #  Простая задача 5.0

    result = True
    
    if number == 1:
        result = False
    elif number == 2:
        result = True
    else:
        for divider in range(3, int(number**0.5) + 2, 2):
            if number % divider == 0:
                result = False
    return result
