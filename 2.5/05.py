def main():
    # Минимальное среднее

    n = int(input())
    
    average_list = [0] * n
    for i in range(n):
        list_sum = 0
        list_length = 0
        while True:
            list_element = input()
            if list_element == "end":
                break
            list_sum += int(list_element)
            list_length += 1
        average_list[i] = list_sum / list_length
        
    result = min(average_list)
    print("{:.2f}".format(result))


if __name__ == "__main__":
    main()
