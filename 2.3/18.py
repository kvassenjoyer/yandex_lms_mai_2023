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
    # Простая задача 2.0

    number = int(input())
    prime_dividers = list(map(str, get_prime_dividers(number)))
    print(" * ".join(prime_dividers))


if __name__ == "__main__":
    main()
