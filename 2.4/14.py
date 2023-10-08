def main():
    # Числовая змейка

    heigth = int(input())
    width = int(input())
    element_width = len(str(heigth * width))
    for i in range(heigth):
        for j in range(width):
            if i % 2 == 1:
                element = i * width + (width - j)
            else:
                element = i * width + (j + 1)
            print(f"{element}".rjust(element_width), end=" ")
        print()


if __name__ == "__main__":
    main()
