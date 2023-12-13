import json


def main():
    # Файловая статистика 2.0

    input_filename = input()
    output_filename = input()

    number_list = []
    with open(input_filename, "r", encoding="UTF-8") as input_file:
        for line in input_file:
            number_list += [int(x) for x in line.split()]

    data = {
        "count": len(number_list),
        "positive_count": len([x for x in number_list if x > 0]),
        "min": min(number_list),
        "max": max(number_list),
        "sum": sum(number_list),
        "average": round(sum(number_list) / len(number_list), 2),
    }

    with open(output_filename, "w", encoding="UTF-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
