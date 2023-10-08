def main():
    # Это будет шедевр!

    n = int(input())

    general_ingredient_set = set()
    for _ in range(n):
        ingredient = input()
        general_ingredient_set.update(ingredient)

    m = int(input())

    dish_to_cook_list = []
    for _ in range(m):
        dish = input()
        number_of_ingredients = int(input())
        dish_ingredient_set = set()
        for _ in range(number_of_ingredients):
            ingredient = input()
            dish_ingredient_set.update(ingredient)

        if dish_ingredient_set & general_ingredient_set == dish_ingredient_set:
            dish_to_cook_list += [dish]

    dish_to_cook_list.sort()
    
    if len(dish_to_cook_list) == 0:
        print("Готовить нечего")
    else:
        for dish in dish_to_cook_list:
            print(dish)


if __name__ == "__main__":
    main()
