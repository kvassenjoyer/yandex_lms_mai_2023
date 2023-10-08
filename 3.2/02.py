def main():
    # Символическая разница

    first_expression = input()
    second_expression = input()

    first_expression_symbols = set()
    for symbol in first_expression:
        first_expression_symbols.update(symbol)

    second_expression_symbols = set()
    for symbol in second_expression:
        second_expression_symbols.update(symbol)

    result_set = first_expression_symbols & second_expression_symbols
    for symbol in result_set:
        print(symbol, end="")


if __name__ == "__main__":
    main()
