def main():
    # Хвост

    input_filename = input()
    n = int(input())

    with open(input_filename, "r", encoding="UTF-8") as input_file:
        print(*input_file.readlines()[-n:], sep="")


if __name__ == "__main__":
    main()
