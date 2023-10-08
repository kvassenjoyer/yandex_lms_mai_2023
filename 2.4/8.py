def main():
    # Максимальная сумма
    
    n = int(input())
    winner_digit_sum = -1
    winner_name = ""
    for _ in range(n):
        name = input()
        number = input()
        digit_sum = sum([int(digit) for digit in number])
        if digit_sum >= winner_digit_sum:
            winner_digit_sum = digit_sum
            winner_name = name
    print(winner_name)


if __name__ == "__main__":
    main()
