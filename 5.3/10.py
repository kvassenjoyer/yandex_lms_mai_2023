import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password,
    min_length=8,
    possible_chars=[
        chr(x)
        for x in [*range(ord("A"), ord("Z") + 1)]
        + [*range(ord("a"), ord("z") + 1)]
        + [*range(ord("0"), ord("9") + 1)]
    ],
    at_least_one=str.isdigit,
):
    if type(password) is not str:
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if not all(x in possible_chars for x in password):
        raise PossibleCharError

    if not any(at_least_one(x) for x in password):
        raise NeedCharError

    password = hashlib.sha256(password.encode("UTF-8"))
    return password.hexdigest()
