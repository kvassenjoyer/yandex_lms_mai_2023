def main():
    # Властелин Чисел: Две Башни

    number = input()

    digits = [int(digit) for digit in number]
    if min(digits) == 0:
        digits.remove(min(digits))
        smaller_number = str(min(digits)) + "0"
    else:
        smaller_number = str(min(digits))
        digits.remove(min(digits))
        smaller_number += str(min(digits))

    digits = [int(digit) for digit in number]
    largest_number = str(max(digits))
    digits.remove(max(digits))
    largest_number += str(max(digits))

    print(smaller_number, largest_number)


if __name__ == "__main__":
    main()
