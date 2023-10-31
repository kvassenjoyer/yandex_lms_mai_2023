def main():
    # Меню питания 2.0

    m = int(input())

    porridge_list = []
    for _ in range(m):
        porridge = input()
        porridge_list += [porridge]

    n = int(input())

    for i in range(n):
        print(porridge_list[i % len(porridge_list)])


if __name__ == "__main__":
    main()
