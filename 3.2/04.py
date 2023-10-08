def main():
    # Кашееды

    n = int(input())
    m = int(input())

    semolina_enjoyer_list = []
    for _ in range(n):
        semolina_enjoyer = input()
        semolina_enjoyer_list += [semolina_enjoyer]

    based_child_counter = 0
    for _ in range(m):
        oatmeal_enjoyer = input()
        if oatmeal_enjoyer in semolina_enjoyer_list:
            based_child_counter += 1

    if based_child_counter == 0:
        print("Таких нет")
    else:
        print(based_child_counter)


if __name__ == "__main__":
    main()
