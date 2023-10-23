def main():
    # Интересный максимум

    n = int(input())
    min_difference = int(input())

    number_list = []
    for _ in range(n):
        number = int(input())
        number_list += [number]
    
    result = None
    for i in range(1, len(number_list)):
        current_difference = abs(number_list[i] - number_list[i - 1])
        if current_difference < min_difference:
            if result is None:
                result = number_list[i]
            elif number_list[i] > result:
                result = number_list[i]
    print(result)


if __name__ == "__main__":
    main()
