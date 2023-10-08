def main():
    # Яблоки

    petya_apples = 7 - 3 + 2
    vasya_apples = 6 + 3

    petya_apples += int(input())
    vasya_apples += int(input())
    if petya_apples > vasya_apples:
        print("Петя")
    else:
        print("Вася")


if __name__ == "__main__":
    main()
