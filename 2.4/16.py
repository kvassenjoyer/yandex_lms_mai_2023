def main():
    # Редизайн таблицы умножения
    
    size = int(input())
    column_width = int(input())
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if column_width % 2 == 0:
                element = str(i * j)
            else:
                element = str(i * j) + " "
            element = element.center(column_width)
            if j != size:
                print(element, end="|")
            else:
                print(element)
        if i != size:
            print("-" * ((column_width + 1) * size - 1))


if __name__ == "__main__":
    main()
