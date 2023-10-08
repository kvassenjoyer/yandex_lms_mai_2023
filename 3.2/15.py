def main():
    # Двоичная статистика!

    number_list = list(map(int, input().split(" ")))

    stat_list = []
    for number in number_list:
        binary_number = bin(number)[2:]
        number_dict = {
            "digits": len(binary_number),
            "units": binary_number.count('1'),
            "zeros": binary_number.count('0')
        }
        stat_list.append(number_dict)

    print(stat_list)


if __name__ == "__main__":
    main()
