def can_eat(horse_position, target_position):
    # Шахматный «обед»

    x_difference = abs(horse_position[0] - target_position[0])
    y_difference = abs(horse_position[1] - target_position[1])

    result = False
    if x_difference**2 + y_difference**2 == 5:
        result = True

    return result
