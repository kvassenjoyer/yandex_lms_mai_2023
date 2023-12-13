import itertools


def main():
    # Словарный комбинатор
    
    alphabet = input().split("; ")
    alphabet = sorted(set(alphabet))
    max_word_lenght = int(input())

    for symbol_tuple in itertools.product(alphabet, repeat=max_word_lenght):
        word = ""
        for symbol in symbol_tuple:
            if symbol not in word:
                word = word + symbol
        if len(word) == max_word_lenght:
            print(word)


if __name__ == "__main__":
    main()
