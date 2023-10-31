import itertools


def main():
    # Список покупок 3.0

    n = int(input())

    product_list = []
    for _ in range(n):
        product_list += input().split(", ")
    product_list.sort()

    for buy_list in itertools.product(product_list, repeat=3):
        if len(buy_list) == len(set(buy_list)):
            print(*buy_list)


if __name__ == "__main__":
    main()
