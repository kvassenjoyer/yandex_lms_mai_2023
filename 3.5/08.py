def main():
    # Файловая разница

    input_filename_list = input(), input()
    output_filename = input()

    word_set_list = []
    for input_filename in input_filename_list:
        word_set = set()
        with open(input_filename, "r", encoding="UTF-8") as input_file:
            for line in input_file:
                word_set.update(line.split())
        word_set_list.append(word_set)
   
    with open(output_filename, "w", encoding="UTF-8") as output_file:
        for word in sorted(word_set_list[0].symmetric_difference(word_set_list[1])):
            print(word, file=output_file)


if __name__ == "__main__":
    main()
