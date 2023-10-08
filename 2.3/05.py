def main():
    # Внимание! Акция!

    total_price = 0
    product_price = -1
    while product_price != 0:
        product_price = float(input())
        if product_price >= 500:
            product_price *= 0.9
        total_price += product_price
    print(total_price)


if __name__ == "__main__":
    main()
