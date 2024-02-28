class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name):

    if type(name) is not str:
        raise TypeError

    cyrillic_indexes = (
        [ord("Ё"), ord("ё")]
        + list(range(ord("А"), ord("Я") + 1))
        + list(range(ord("а"), ord("я") + 1))
    )
    if not all(ord(x) in cyrillic_indexes for x in name):
        raise CyrillicError

    if name != name.capitalize():
        raise CapitalError

    return name


def username_validation(username):

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


def user_validation(*args, last_name=None, first_name=None, username=None, **kwargs):
    # Валидация пользователя

    if len(args) != 0 or len(kwargs) != 0 or None in [last_name, first_name, username]:
        raise KeyError

    if not all(isinstance(x, str) for x in [last_name, first_name, username]):
        raise TypeError

    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)

    user_dict = {"last_name": last_name, "first_name": first_name, "username": username}
    return user_dict
