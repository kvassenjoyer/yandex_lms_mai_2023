def main():
    # Друзья друзей

    friend_dict = {}

    line = input()
    while line != "":
        first, second = line.split(" ")
        if first not in friend_dict.keys():
            friend_dict[first] = []
        if second not in friend_dict[first]:
            friend_dict[first] += [second]

        if second not in friend_dict.keys():
            friend_dict[second] = []
        if first not in friend_dict[second]:
            friend_dict[second] += [first]

        line = input()

    friend_dict = dict(sorted(friend_dict.items()))

    for name, friend_list in friend_dict.items():
        friend_of_friend_list = []
        for friend_name in friend_list:
            for friend_of_friend_name in friend_dict[friend_name]:
                if friend_of_friend_name not in friend_of_friend_list:
                    if friend_of_friend_name not in friend_list + [name]:
                        friend_of_friend_list += [friend_of_friend_name]
        friend_of_friend_list.sort()

        print(name, end=": ")
        print(*friend_of_friend_list, sep=", ")


if __name__ == "__main__":
    main()
