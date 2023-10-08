def main():
    # Украшение чека

    product_name = input()
    price_of_kg = int(input())
    weight_kg = int(input())
    price = weight_kg * price_of_kg
    payment = int(input())
    line_len = 35

    print("Чек".center(line_len, '='))
    print("Товар:" + f"{product_name}".rjust(line_len - 6, " "))
    print("Цена:" + f"{weight_kg}кг * {price_of_kg}руб/кг".rjust(line_len - 5, " "))
    print("Итого:" + f"{price}руб".rjust(line_len - 6, " "))
    print("Внесено:" + f"{payment}руб".rjust(line_len - 8, " "))
    print("Сдача:" + f"{payment-price}руб".rjust(line_len - 6, " "))
    print("=" * line_len)


if __name__ == "__main__":
    main()
