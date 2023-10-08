def main():
    # Сильная цифра

    number = input()
    digits = [int(digit) for digit in number]
    print(max(digits))


if __name__ == "__main__":
    main()
