def is_nice(number):
    digits = [int(digit) for digit in str(number)]
    if 3 * max(digits) + 3 * min(digits) == 2 * sum(digits):
        print("YES")
    else:
        print("NO")


def main():
    # Красота спасёт мир

    number = int(input())
    is_nice(number)


if __name__ == "__main__":
    main()
