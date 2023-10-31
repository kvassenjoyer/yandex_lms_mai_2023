def main():
    # Словарная ёлка

    word_list = input().split()

    line = ""
    for word in word_list:
        line = line + word + " "
        print(line)


if __name__ == "__main__":
    main()
