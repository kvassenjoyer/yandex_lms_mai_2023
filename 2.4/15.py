def main():
    # Числовая змейка 2.0

    heigth = int(input())
    width = int(input())
    element_width = len(str(heigth * width))
    for i in range(heigth):
        for j in range(width):
            if j % 2 == 1:
                element = j * heigth + (heigth - i)
            else:
                element = j * heigth + i + 1
            print(f"{element}".rjust(element_width), end=" ")
        print()


if __name__ == "__main__":
    main()
