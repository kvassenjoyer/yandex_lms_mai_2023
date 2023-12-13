def main():
    # Файловая статистика

    input_filename = input()

    number_list = []
    with open(input_filename, "r", encoding="UTF-8") as input_file:
        for line in input_file:
            number_list += map(int, line.split())

    number_amount = len(number_list)
    positive_number_amount = len([x for x in number_list if x > 0])
    min_number = min(number_list)
    max_number = max(number_list)
    number_sum = sum(number_list)
    number_average = round(number_sum / number_amount, 2)

    print(
        number_amount,
        positive_number_amount,
        min_number,
        max_number,
        number_sum,
        number_average,
        sep="\n",
    )


if __name__ == "__main__":
    main()
