import itertools


def multiple_sum(*numbers, div=2):
    # Кратное суммирование

    result = None
    for i in range(len(numbers) + 1):
        for x in itertools.combinations(numbers, r=i):
            if (sum(x) % div == 0) and (result is None or sum(x) > result):
                result = sum(x)
    return result
