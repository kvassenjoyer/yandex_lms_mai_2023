def main():
    # Числовой прямоугольник 2.0
    
    heigth = int(input())
    width = int(input())
    element_width = len(str(heigth * width))
    for i in range(heigth):
        for j in range(width):
            print(f"{i+1+j*heigth}".rjust(element_width), end=" ")
        print()


if __name__ == "__main__":
    main()
