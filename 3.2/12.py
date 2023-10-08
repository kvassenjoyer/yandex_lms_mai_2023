def main():
    # Однофамильцы — 2

    n = int(input())
    surname_dict = {}

    for _ in range(n):
        surname = input()
        if surname not in surname_dict.keys():
            surname_dict[surname] = 1
        else:
            surname_dict[surname] += 1

    surname_dict = dict(sorted(surname_dict.items()))

    is_namesakes_in_team = False
    for surname, surname_counter in surname_dict.items():
        if surname_counter != 1:
            is_namesakes_in_team = True
            print(f"{surname} - {surname_counter}")

    if is_namesakes_in_team is False:
        print("Однофамильцев нет")


if __name__ == "__main__":
    main()
