def main():
    # Символическая выжимка

    expression = input()
    symbol_list = []

    for symbol in expression:
        if symbol not in symbol_list:
            symbol_list += [symbol]

    for symbol in symbol_list:
        print(symbol, end="")


if __name__ == "__main__":
    main()
