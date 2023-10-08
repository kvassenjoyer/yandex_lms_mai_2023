def main():
    # Считалочка 2.0

    start, finish = [int(input()) for _ in range(2)]

    if finish > start:
        step, finish = 1, finish + 1
    else:
        step, finish = -1, finish - 1

    for number in range(start, finish, step):
        print(number, end=" ")
    print()


if __name__ == "__main__":
    main()
