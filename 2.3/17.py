def main():
    # Чётная чистота

    number = input()
    digits = [digit for digit in number if int(digit) % 2 == 1]
    print("".join(digits))


if __name__ == "__main__":
    main()
