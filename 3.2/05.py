def main():
    # Кашееды — 2

    n = int(input())
    m = int(input())

    porridge_enjoyer_dict = {}
    for _ in range(n + m):
        name = input()
        if name not in porridge_enjoyer_dict.keys():
            porridge_enjoyer_dict[name] = 1
        else:
            porridge_enjoyer_dict[name] += 1

    is_all_children_based = True
    porridge_beginner_counter = 0
    for name, porridge_counter in porridge_enjoyer_dict.items():
        if porridge_counter == 1:
            is_all_children_based = False
            porridge_beginner_counter += 1

    if is_all_children_based:
        print("Таких нет")
    else:
        print(porridge_beginner_counter)


if __name__ == "__main__":
    main()
