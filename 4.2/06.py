def order(*args):
    # Кофейня
    
    global in_stock

    menu = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
    }

    result_dish = "К сожалению, не можем предложить Вам напиток"

    for dish in args:
        is_dish_cookable = True

        for ingredient in menu[dish].keys():
            if in_stock[ingredient] < menu[dish][ingredient]:
                is_dish_cookable = False

        if is_dish_cookable is True:
            for ingredient in menu[dish].keys():
                in_stock[ingredient] -= menu[dish][ingredient]
            result_dish = dish
            break

    return result_dish
