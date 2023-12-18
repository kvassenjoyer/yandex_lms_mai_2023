def rindex(text: str):
    # Генератор вхождений

    symbols = [chr(x) for x in range(65, 91)]
    symbols += [chr(x) for x in range(97, 123)]
    symbols += [chr(x) for x in range(1040, 1072)]
    symbols += [chr(x) for x in range(1072, 1104)]

    for symbol in symbols:
        if symbol in text:
            yield (symbol, text.rfind(symbol))
