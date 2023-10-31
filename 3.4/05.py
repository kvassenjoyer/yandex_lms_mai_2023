def main():
    # Список покупок

    product_list = []
    for _ in range(3):
        product_list += input().split(", ")
    product_list.sort()

    for i, product in enumerate(product_list):
        print(f"{i + 1}. {product}")


if __name__ == "__main__":
    main()
