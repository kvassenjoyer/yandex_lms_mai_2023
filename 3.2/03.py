def main():
    # Зайка — 8

    n = int(input())
    terrain_list = []

    for _ in range(n):
        line = input()
        for word in line.split(" "):
            if word not in terrain_list:
                terrain_list += [word]

    for terrain in terrain_list:
        print(terrain)


if __name__ == "__main__":
    main()
