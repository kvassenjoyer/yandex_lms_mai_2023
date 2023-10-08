def main():
    # Цифровая сумма

    number = input()
    digits = [int(digit) for digit in number]
    print(sum(digits))


if __name__ == "__main__":
    main()
