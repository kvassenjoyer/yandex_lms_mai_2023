def main():
    # Властелин Чисел: Братство общей цифры

    # работает для чисел любой единой длины
    number_list = [input() for _ in range(3)]
    digits_in_number = len(number_list[0])

    for digit_index in range(digits_in_number):
        common_digit = number_list[0][digit_index]
        flag = True
        for number_index in range(len(number_list)):
            if number_list[number_index][digit_index] != common_digit:
                flag = False
        if flag:
            print(common_digit)
            break


if __name__ == "__main__":
    main()
