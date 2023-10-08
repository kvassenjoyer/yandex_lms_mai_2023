def main():
    # Мухи отдельно, котлеты отдельно

    total_weight = int(input())
    total_price_per_kg = int(input())
    first_price_per_kg = int(input())
    second_price_per_kg = int(input())

    first_weight = int(
        total_weight
        * (total_price_per_kg - second_price_per_kg)
        / (first_price_per_kg - second_price_per_kg)
    )
    second_weight = total_weight - first_weight
    print(first_weight, second_weight)


if __name__ == "__main__":
    main()
