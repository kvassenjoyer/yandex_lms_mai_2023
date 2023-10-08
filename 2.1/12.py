def main():
    # Интересное сложение

    long_number = [int(c) for c in input()]
    short_number = [int(c) for c in input()]
    small_lenght = len(short_number)
    big_lenght = len(long_number)

    if big_lenght < small_lenght:
        long_number, short_number = short_number, long_number

    result = [0] * big_lenght
    for index in range(1, big_lenght + 1):
        result[-index] = long_number[-index]
        if index <= small_lenght:
            result[-index] += short_number[-index]
        result[-index] = result[-index] % 10

    for digit in result:
        print(digit, end="")


if __name__ == "__main__":
    main()
