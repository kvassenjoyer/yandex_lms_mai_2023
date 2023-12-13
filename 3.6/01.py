def main():
    # Шинковка строк
    
    n = int(input())

    for _ in range(n):
        package = input()
        expression, start_index, finish_index = package.split("^")
        start_index, finish_index = int(start_index), int(finish_index)
        step_size = len(expression) % 4
        for symbol_index in range(
            start_index, min(len(expression), finish_index), step_size
        ):
            print(expression[symbol_index], end="")
        print()


if __name__ == "__main__":
    main()
