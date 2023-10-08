def get_number_digit_sum_in_base(number, base):
    base_number = ""
    while number > 0:
        base_number = str(number % base) + base_number
        number = number // base
    return sum([int(digit) for digit in base_number])


def main():
    # Математическая выгода
    
    number = int(input())
    max_digit_sum = get_number_digit_sum_in_base(number, 2)
    result = 2
    for base in range(3, 11):
        digit_sum = get_number_digit_sum_in_base(number, base)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            result = base
    print(result)


if __name__ == "__main__":
    main()
