def main():
    # Это будет наш секрет

    shift = int(input())
    output_message = ""

    with open("public.txt", "r", encoding="UTF-8") as file:
        input_message = file.read()
        for symbol in input_message:
            # Explanation: ord("A") == 65; ord("Z") == 90; ord("a") == 97; ord("z") == 122
            if 65 <= ord(symbol) <= 90:
                output_message += chr(65 + (ord(symbol) - 65 + shift) % (90 - 65 + 1))
            elif 97 <= ord(symbol) <= 122:
                output_message += chr(97 + (ord(symbol) - 97 + shift) % (122 - 97 + 1))
            else:
                output_message += symbol

    with open("private.txt", "w") as file_out:
        print(output_message, file=file_out)


if __name__ == "__main__":
    main()
