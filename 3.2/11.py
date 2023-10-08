def main():
    # Однофамильцы

    n = int(input())
    surname_dict = {}

    for _ in range(n):
        surname = input()
        if surname not in surname_dict.keys():
            surname_dict[surname] = 1
        else:
            surname_dict[surname] += 1

    namesake_counter = 0
    for surname, surname_counter in surname_dict.items():
        if surname_counter != 1:
            namesake_counter += surname_counter

    print(namesake_counter)


if __name__ == "__main__":
    main()
