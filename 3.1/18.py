def main():
    # RLE

    expression = input()

    counter = 0
    previous_symbol = expression[0]
    for symbol in expression:
        if previous_symbol != symbol:
            print(previous_symbol, counter)
            previous_symbol = symbol
            counter = 0
        counter += 1
    print(previous_symbol, counter)


if __name__ == "__main__":
    main()
