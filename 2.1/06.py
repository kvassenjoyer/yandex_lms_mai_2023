def main():
    # Чек

    product_name = input()
    price_of_kg = int(input())
    weight_kg = int(input())
    payment = int(input())
    price = weight_kg * price_of_kg

    print("Чек")
    print(f"{product_name} - {weight_kg}кг - {price_of_kg}руб/кг")
    print(f"Итого: {price}руб")
    print(f"Внесено: {payment}руб")
    print(f"Сдача: {payment-price}руб")


if __name__ == "__main__":
    main()
