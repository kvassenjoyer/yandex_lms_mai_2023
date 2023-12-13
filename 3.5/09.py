def main():
    # Файловая чистка

    input_filename = input()
    output_filename = input()

    with open(input_filename, "r", encoding="UTF-8") as input_file:
        with open(output_filename, "w", encoding="UTF-8") as output_file:
            for line in input_file:
                line = line.strip().replace("\t", "")
                word_list = line.split()
                if len(word_list) != 0:
                    print(*word_list, file=output_file)


if __name__ == "__main__":
    main()
