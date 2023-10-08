def main():
    # Дайте чего-нибудь новенького!

    n = int(input())

    possible_dish_list = []
    for _ in range(n):
        dish = input()
        possible_dish_list += [dish]

    m = int(input())

    dish_to_cook_list = possible_dish_list.copy()
    for _ in range(m):
        day_dish_amount = int(input())
        for _ in range(day_dish_amount):
            dish = input()
            if dish in dish_to_cook_list:
                dish_to_cook_list.remove(dish)

    dish_to_cook_list.sort()
    for dish in dish_to_cook_list:
        print(dish)

    if len(dish_to_cook_list) == 0:
        print("Готовить нечего")


if __name__ == "__main__":
    main()
