def get_nod(a, b):
    while a != 0:
        if b < a:
            a, b = b, a
        a, b = b - a, a
    return b


def main():
    # НОД 3.0

    number_list = [int(elem) for elem in str(input()).split(" ")]
    result = get_nod(number_list[0], number_list[1])
    for i in range(2, len(number_list)):
        result = get_nod(result, number_list[i])
    print(result)


if __name__ == "__main__":
    main()
