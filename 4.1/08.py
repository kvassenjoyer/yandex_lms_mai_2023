def is_palindrome(x):
    # А роза упала на лапу Азора 7.0

    result = False
    if type(x) is int and str(x) == str(x)[::-1]:
        result = True
    elif type(x) in (str, tuple, list) and x == x[::-1]:
        result = True

    return result
