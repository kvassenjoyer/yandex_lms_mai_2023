def main():
    # Кашееды — 3

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
    porridge_beginner_list = []
    for name, porridge_counter in porridge_enjoyer_dict.items():
        if porridge_counter == 1:
            is_all_children_based = False
            porridge_beginner_list += [name]

    if is_all_children_based:
        print("Таких нет")
    else:
        porridge_beginner_list.sort()
        for name in porridge_beginner_list:
            print(name)


if __name__ == "__main__":
    main()
