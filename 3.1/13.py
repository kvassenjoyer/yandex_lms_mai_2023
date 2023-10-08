def main():
    # Массовое возведение в степень

    n = int(input())
    number_list = []

    for i in range(n):
        number = int(input())
        number_list.append(number)

    power_value = int(input())

    for number in number_list:
        print(pow(number, power_value))


if __name__ == "__main__":
    main()
