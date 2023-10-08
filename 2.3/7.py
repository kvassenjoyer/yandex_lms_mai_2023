def get_prime_dividers(number):
    dividers = []
    divider = 2
    while number != 1:
        if number % divider == 0:
            dividers.append(divider)
            number = number / divider
            divider = 2
        else:
            divider += 1
    return dividers


def main():
    # НОК

    a, b = [int(input()) for _ in range(2)]
    a_dividers = get_prime_dividers(a)
    b_dividers = get_prime_dividers(b)

    result_dividers = a_dividers.copy()
    for divider in b_dividers:
        if b_dividers.count(divider) > result_dividers.count(divider):
            result_dividers.append(divider)

    result = 1
    for divider in result_dividers:
        result *= divider
    print(result)


if __name__ == "__main__":
    main()
