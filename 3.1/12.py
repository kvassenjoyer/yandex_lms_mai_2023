def main():
    # Меню питания

    n = int(input())
    cereal_list = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    cereal_list_len = len(cereal_list)

    for i in range(n):
        print(cereal_list[i % cereal_list_len])


if __name__ == "__main__":
    main()
