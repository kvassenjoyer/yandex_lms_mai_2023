def main():
    # Числовое колебание

    n = int(input())
    m = int(input())
    d = int(input())

    number_list = []
    for number in range(n, m + 1, d):
        number_list += [str(number)]

    number_list = number_list + number_list[::-1]
    print(" - ".join(number_list))


if __name__ == "__main__":
    main()
