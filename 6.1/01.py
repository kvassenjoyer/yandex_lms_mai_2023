import math


def f(x):
    return (
        math.log(math.pow(x, 3 / 16), 32)
        + pow(x, math.cos(math.pi * x / (2 * math.e)))
        - pow(math.sin(x / math.pi), 2)
    )


def main():
    # Математика — круто, но это не точно

    x = float(input())
    print(f(x))


if __name__ == "__main__":
    main()
