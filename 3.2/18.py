def main():
    # Карта сокровищ

    n = int(input())

    equivalence_class_dict = {}
    for _ in range(n):
        x, y = map(int, input().split(" "))
        equivalence_class_dict = (x // 10, y // 10)
        if equivalence_class_dict not in equivalence_class_dict:
            equivalence_class_dict[equivalence_class_dict] = 0
        equivalence_class_dict[equivalence_class_dict] += 1

    largest_equivalence_class_capacity = sorted(equivalence_class_dict.values())[-1]
    print(largest_equivalence_class_capacity)


if __name__ == "__main__":
    main()
