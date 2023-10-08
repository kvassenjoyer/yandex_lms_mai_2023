def main():
    # Анонс новости 2.0

    postfix = "..."
    postfix_len = len(postfix)
    title_len = int(input())
    n = int(input())

    for i in range(n):
        title = str(input())
        if title_len - len(title) <= postfix_len:
            print(title[:title_len - postfix_len] + postfix)
            break
        else:
            print(title)
        title_len -= len(title)


if __name__ == "__main__":
    main()
