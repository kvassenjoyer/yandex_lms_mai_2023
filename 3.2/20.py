def get_nod(a, b):
    while a != 0:
        if b < a:
            a, b = b, a
        a, b = b - a, a
    return b


def main():
    # Простая задача 4.0

    number_list = sorted(set(map(int, input().split("; "))))

    for line_number in number_list:
        mutually_prime_list = []
        for number in number_list:
            if get_nod(line_number, number) == 1:
                mutually_prime_list += [number]

        if len(mutually_prime_list) != 0:
            print(line_number, end=" - ")
            print(*mutually_prime_list, sep=", ")


if __name__ == "__main__":
    main()
