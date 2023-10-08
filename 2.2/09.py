def main():
    # Первому игроку приготовиться

    amount_of_players = 3
    name_list = [input() for _ in range(amount_of_players)]

    first_player = sorted(name_list)[0]
    print(first_player)


if __name__ == "__main__":
    main()
