def main():
    # Зайка — 9

    line = input()
    terrain_dict = {}
    while line != "":
        for terrain in line.split(" "):
            if terrain not in terrain_dict.keys():
                terrain_dict[terrain] = 1
            else:
                terrain_dict[terrain] += 1
        line = input()

    for key, value in terrain_dict.items():
        print(key, value)


if __name__ == "__main__":
    main()
