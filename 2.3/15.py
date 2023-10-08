def main():
    # Зайка - 4

    target = "зайка"
    counter = 0
    n = int(input())
    for _ in range(n):
        sentence = input()
        if target in sentence:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
