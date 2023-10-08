def main():
    # НОД

    a, b = [int(input()) for _ in range(2)]

    while a != 0:
        if b < a:
            a, b = b, a
        a, b = b - a, a
    print(b)


if __name__ == "__main__":
    main()
