def main():
    # Транслитерация 2.0

    transliteration_dict = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ъ": "",
        "Ы": "Y",
        "Ь": "",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
    }

    input_filename = "cyrillic.txt"
    output_filename = "transliteration.txt"

    input_line_list = []
    output_line_list = []

    with open(input_filename, "r", encoding="UTF-8") as input_file:
        for line in input_file:
            input_line_list.append(line.strip())

    for line in input_line_list:
        output_line = ""
        for symbol in line:
            if symbol.upper() in transliteration_dict.keys():
                if symbol.upper() == symbol:
                    output_line += transliteration_dict[symbol].lower().capitalize()
                else:
                    output_line += transliteration_dict[symbol.upper()].lower()
            else:
                output_line = output_line + symbol
        output_line_list.append(output_line)

    with open(output_filename, "w", encoding="UTF-8") as output_file:
        print(*output_line_list, sep="\n", file=output_file)


if __name__ == "__main__":
    main()
