def main():
    # Считалочка

    start, finish = [int(input()) for _ in range(2)]
    for number in range(start, finish + 1):
        print(number, end=" ")
    print()


if __name__ == "__main__":
    main()
