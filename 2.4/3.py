def main():
    # Новогоднее настроение
    
    n = int(input())
    first_in_line = 1
    line_length = 1
    while first_in_line <= n:
        for number in range(first_in_line, min(n, first_in_line + line_length - 1) + 1):
            print(number, end=" ")
        first_in_line += line_length
        line_length += 1
        print()


if __name__ == "__main__":
    main()
