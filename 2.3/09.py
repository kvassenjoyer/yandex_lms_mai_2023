def get_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def main():
    # Факториал

    number = int(input())
    print(get_factorial(number))


if __name__ == "__main__":
    main()
