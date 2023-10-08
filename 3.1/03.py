def main():
    # Анонс новости
    
    max_length = int(input())
    n = int(input())

    for _ in range(n):
        title = input()
        if len(title) > max_length:
            print(title[:max_length - 3] + "...")
        else:
            print(title)


if __name__ == "__main__":
    main()
