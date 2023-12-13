def main():
    # Словарная опись

    line = input()
    word_dict = {}
    while line != "":
        for word in line.split():
            if len(word) % 2 == 0:
                word_key = word[len(word) // 2 - 1]
            else:
                word_key = word[len(word) // 2]
            word_key = word_key.lower()
            if word_key not in word_dict.keys():
                word_dict[word_key] = [word.upper()]
            elif word.upper() not in word_dict[word_key]:
                word_dict[word_key] += [word.upper()]
        line = input()
    for key in word_dict.keys():
        word_dict[key].sort()
        print(key, '"', end="")
        print(*word_dict[key], sep=". ", end='"\n')


if __name__ == "__main__":
    main()
