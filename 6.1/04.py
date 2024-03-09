import math


def get_geom_mean(*args):
    result = 1
    for x in args:
        result *= x
    result = math.pow(result, 1 / len(args))
    return result


def main():
    # Среднее не арифметическое

    numbers = [float(x) for x in input().split()]
    print(get_geom_mean(*numbers))


if __name__ == "__main__":
    main()
