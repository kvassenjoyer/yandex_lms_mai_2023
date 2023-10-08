def is_on_island(x, y):
    return x * x + y * y < 100


def is_in_danger_zone(x, y):
    condition_1 = x * x + y * y < 25
    condition_2 = y < 5 / 3 * x + 35 / 3
    condition_3 = y > 0.25 * (x + 1) * (x + 1) - 9
    return condition_1 and condition_2 and condition_3


def main():
    # Автоматизация безопасности

    x, y = [float(input()) for _ in range(2)]

    if is_in_danger_zone(x, y):
        print("Опасность! Покиньте зону как можно скорее!")
    elif is_on_island(x, y):
        print("Зона безопасна. Продолжайте работу.")
    else:
        print("Вы вышли в море и рискуете быть съеденным акулой!")


if __name__ == "__main__":
    main()
