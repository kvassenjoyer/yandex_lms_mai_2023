def main():
    # Игровая сетка

    n = int(input())

    player_name_list = []
    for _ in range(n):
        player_name = input()
        player_name_list += [player_name]

    for i in range(len(player_name_list)):
        for j in range(i + 1, len(player_name_list)):
            print(f"{player_name_list[i]} - {player_name_list[j]}")


if __name__ == "__main__":
    main()
