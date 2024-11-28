import itertools
import math


def main():
    # Таблица умножения 3.0

    n = int(input())

    for element in itertools.product(range(1, n + 1), repeat=2):
        if element[-1] == n:
            print(math.prod(element))
        else:
            print(math.prod(element), end=" ")


if __name__ == "__main__":
    main()
