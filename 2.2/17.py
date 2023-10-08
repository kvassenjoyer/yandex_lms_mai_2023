def main():
    # Корень зла

    a, b, c = [float(input()) for _ in range(3)]
    discriminant = b * b - 4 * a * c
    root_list = []
    if a == 0 and b == 0 and c == 0:
        print("Infinite solutions")
    elif a == 0 and b == 0:
        print("No solution")
    elif a == 0:
        root = -c / b
        root_list += [root]
    elif discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        root = -b / (2 * a)
        root_list += [root]
    else:
        first_root = (-b - discriminant**0.5) / (2 * a)
        second_root = (-b + discriminant**0.5) / (2 * a)
        root_list += [first_root, second_root]

    for number in sorted(root_list):
        print(f"{number:.2f}", end=" ")
    print()


if __name__ == "__main__":
    main()
