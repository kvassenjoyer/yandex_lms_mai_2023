def main():
    # Максимальная сумма
    
    n = int(input())
    result_number = ""
    for _ in range(n):
        number = input()
        max_digit = max([int(digit) for digit in number])
        result_number = result_number + str(max_digit)
    print(result_number)


if __name__ == "__main__":
    main()
