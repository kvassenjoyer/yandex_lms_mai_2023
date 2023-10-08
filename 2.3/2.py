def main():
    # Зайка — 3

    target = "зайка"
    counter = 0
    sentence = ""

    while sentence != "Приехали!":
        sentence = input()
        if target in sentence:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()

