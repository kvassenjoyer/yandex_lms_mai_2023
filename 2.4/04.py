def main():
    # Суммарная сумма
    
    n = int(input())
    result = 0
    for _ in range(n):
        number = input()
        for digit in number:
            result += int(digit)
    print(result)


if __name__ == "__main__":
    main()
