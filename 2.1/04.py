def main():
    # Сдача

    weight_kg = 2.5
    price_of_kg = 38
    price = int(weight_kg * price_of_kg)
    payment = int(input())
    print(payment - price)


if __name__ == "__main__":
    main()
