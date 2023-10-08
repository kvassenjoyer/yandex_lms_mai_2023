def main():
    # Властелин Чисел: Возвращение Цезаря

    first_number = input()
    second_number = input()
    digits = [int(digit) for digit in first_number + second_number]
    digits = sorted(digits, reverse=True)

    first_digit = digits[0]
    second_number = sum(digits[1:-1]) % 10
    third_digit = digits[-1]
    print(str(first_digit) + str(second_number) + str(third_digit))


if __name__ == "__main__":
    main()
