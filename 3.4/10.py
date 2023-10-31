def main():
    # Мы делили апельсин 2.0

    n = int(input())

    print("А Б В")
    for a in range(1, n):
        for b in range(1, n - a):
            print(a, b, n - a - b)


if __name__ == "__main__":
    main()
