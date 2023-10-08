def main():
    # Магазин

    price_of_kg = int(input())
    weight_kg = int(input())
    payment = int(input())
    print(payment - weight_kg * price_of_kg)


if __name__ == "__main__":
    main()
