class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    # Валидация имени пользователя

    if type(username) is not str:
        raise TypeError

    allowed_char_indexes = (
        [ord("_")]
        + list(range(ord("A"), ord("Z") + 1))
        + list(range(ord("a"), ord("z") + 1))
        + list(range(ord("0"), ord("9") + 1))
    )

    if not all(ord(x) in allowed_char_indexes for x in username):
        raise BadCharacterError

    if any(username.startswith(str(i)) for i in range(10)):
        raise StartsWithDigitError

    return username
   