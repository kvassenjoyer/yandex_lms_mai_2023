def encrypt(number):
    ones, tens, hundreds = [int(digit) for digit in str(number)]

    if ones + tens >= hundreds + tens:
        number = str(ones + tens) + str(hundreds + tens)
    else:
        number = str(hundreds + tens) + str(ones + tens)
    return int(number)


def main():
    # Лучшая защита — шифрование

    number = int(input())
    print(encrypt(number))


if __name__ == "__main__":
    main()
