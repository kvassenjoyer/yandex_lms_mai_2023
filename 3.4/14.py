import itertools


def main():
    # Спортивные гадания

    n = int(input())

    name_list = []
    for _ in range(n):
        name = input()
        name_list += [name]
    name_list.sort()

    for p in itertools.product(name_list, repeat=3):
        if len(p) == len(set(p)):
            print(*p, sep=", ")


if __name__ == "__main__":
    main()
