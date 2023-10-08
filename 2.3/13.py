def main():
    # Первому игроку приготовиться 2.0

    n = int(input())
    name_list = [input() for _ in range(n)]
    first_player = sorted(name_list)[0]
    print(first_player)


if __name__ == "__main__":
    main()
