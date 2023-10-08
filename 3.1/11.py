def main():
    # Найдётся всё

    n = int(input())
    title_list = []
    for i in range(n):
        title = input()
        title_list.append(title)
    target = input()
    for title in title_list:
        if target.lower() in title.lower():
            print(title)


if __name__ == "__main__":
    main()
