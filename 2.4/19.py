def main():
    # Числовой квадрат
    
    n = int(input())

    if n % 2 == 1:
        max_value = n // 2 + 1
    else:
        max_value = n // 2 + 0.5
    element_width = len(str(int(max_value)))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            element = max_value - max(abs(max_value - i), abs(max_value - j))
            element = str(int(element)).rjust(element_width)
            print(element, end=" ")
        print()


if __name__ == "__main__":
    main()
