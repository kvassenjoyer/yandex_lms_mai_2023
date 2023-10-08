def main():
    # Частная собственность

    n = int(input())

    toy_dict = {}
    for _ in range(n):
        name, toy_str = input().split(": ")
        toy_list = set(toy_str.split(", "))

        for toy in toy_list:
            if toy not in toy_dict:
                toy_dict[toy] = 0
            toy_dict[toy] += 1

    toy_dict = dict(sorted(toy_dict.items()))

    for toy, counter in toy_dict.items():
        if counter == 1:
            print(toy)


if __name__ == "__main__":
    main()
