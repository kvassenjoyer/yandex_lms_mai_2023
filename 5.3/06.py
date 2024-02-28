class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    # Корень зла 2

    if not all(type(x) in [int, float] for x in [a, b, c]):
        raise TypeError

    discriminant = b * b - 4 * a * c
    root_tuple = ()

    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError
    elif a == 0 and b == 0:
        raise NoSolutionsError
    elif a == 0:
        root = -c / b
        root_tuple = root
    elif discriminant < 0:
        raise NoSolutionsError
    elif discriminant == 0:
        root = -b / (2 * a)
        root_tuple = (root, root)
    else:
        first_root = (-b - discriminant**0.5) / (2 * a)
        second_root = (-b + discriminant**0.5) / (2 * a)
        root_tuple = (first_root, second_root)

    return root_tuple
