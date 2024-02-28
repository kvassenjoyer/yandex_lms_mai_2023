class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    # Валидация имени

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
