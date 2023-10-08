def main():
    # Зайка — 10

    target = "зайка"
    next_to_target_list = []

    line = "anekdot"
    while line != "":
        line = input()
        terrain_list = line.split(" ")
        terrain_amount = len(terrain_list)
        for i in range(terrain_amount):
            if (terrain_list[i] == target):
                if (i != 0) and (terrain_list[i - 1] not in next_to_target_list):
                    next_to_target_list.append(terrain_list[i - 1])
                if (i != terrain_amount - 1) and (terrain_list[i + 1] not in next_to_target_list):
                    next_to_target_list.append(terrain_list[i + 1])

    for terrain in next_to_target_list:
        print(terrain)


if __name__ == "__main__":
    main()
