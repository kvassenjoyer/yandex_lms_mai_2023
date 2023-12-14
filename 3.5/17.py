def main():
    # Прятки

    with open("secret.txt", "r", encoding="UTF-8") as file:
        file_content = file.read()
        for symbol in file_content:
            print(chr(ord(symbol) % 128), end="")


if __name__ == "__main__":
    main()
