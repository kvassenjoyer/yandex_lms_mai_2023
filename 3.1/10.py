def main():
    # Частотный анализ на минималках
    
    line = ""
    symbols_frequency = {' ': 0}
    while line != "ФИНИШ":
        line = line.replace(" ", "")
        for symbol in line:
            symbol = symbol.lower()
            if symbol in symbols_frequency.keys():
                symbols_frequency[symbol] += 1
            else:
                symbols_frequency[symbol] = 1
        line = input()
    symbols_frequency = dict(sorted(symbols_frequency.items(), key=lambda item: ord(item[0])))
    symbols_frequency = dict(sorted(symbols_frequency.items(), key=lambda item: -item[1]))
    print(list(symbols_frequency.keys())[0])


if __name__ == "__main__":
    main()
