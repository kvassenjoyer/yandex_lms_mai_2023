def is_triangle(*sides):
    if 2 * max(sides) < sum(sides):
        print("YES")
    else:
        print("NO")


def main():
    # Музыкальный инструмент

    first_side = int(input())
    second_side = int(input())
    third_side = int(input())
    is_triangle(first_side, second_side, third_side)


if __name__ == "__main__":
    main()
