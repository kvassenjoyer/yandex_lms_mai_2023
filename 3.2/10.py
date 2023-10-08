def main():
    # Транслитерация

    transliteration_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
        'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH',
        'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'IU', 'Я': 'IA'
    }

    expression = input()
    transliteration = ""
    for symbol in expression:
        if symbol in transliteration_dict.keys():
            transliteration = transliteration + transliteration_dict[symbol].capitalize()
        elif symbol.upper() in transliteration_dict.keys():
            transliteration = transliteration + transliteration_dict[symbol.upper()].lower()
        else:
            transliteration = transliteration + symbol
    print(transliteration)


if __name__ == "__main__":
    main()
