def main():
    # Дед Мороз и конфеты

    number_of_children = int(input())
    number_of_sweets = int(input())
    sweets_per_children = number_of_sweets // number_of_children
    change = number_of_sweets - sweets_per_children * number_of_children
    print(sweets_per_children)
    print(change)


if __name__ == "__main__":
    main()
