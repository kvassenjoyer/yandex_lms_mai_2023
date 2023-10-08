def main():
    # Массовое возведение в степень 2.0

    number_list = [int(elem) for elem in str(input()).split(" ")]
    power_value = int(input())

    for number in number_list:
        print(pow(number, power_value), end=" ")


if __name__ == "__main__":
    main()
