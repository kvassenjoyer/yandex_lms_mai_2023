def main():
    # Кашееды — 4

    n = int(input())

    group_porridge_dict = {}
    for _ in range(n):
        porridge_list = []
        expression = input()
        name = expression.split(" ")[0]
        group_porridge_dict[name] = expression.split(" ")[1:]

    group_porridge_dict = dict(sorted(group_porridge_dict.items()))

    target_porridge = input()
    is_someone_likes_target = False
    for name, porridge_list in group_porridge_dict.items():
        if target_porridge in porridge_list:
            is_someone_likes_target = True
            print(name)

    if is_someone_likes_target is False:
        print("Таких нет")


if __name__ == "__main__":
    main()
