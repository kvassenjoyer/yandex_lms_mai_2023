def main():
    # Автоматизация списка

    expression = input()

    for i, word in enumerate(expression.split()):
        print(f"{i + 1}. {word}")


if __name__ == "__main__":
    main()
