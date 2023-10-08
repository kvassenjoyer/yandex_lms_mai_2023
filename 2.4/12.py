def main():
    # Числовой прямоугольник
    
    heigth = int(input())
    width = int(input())
    element_width = len(str(heigth * width))
    number = 1
    for _ in range(heigth):
        for _ in range(width):
            print(f"{number}".rjust(element_width), end=" ")
            number += 1
        print()


if __name__ == "__main__":
    main()
