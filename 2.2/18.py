def is_triangle(*sides):
    if 2 * max(sides) < sum(sides):
        return True
    else:
        return False


def main():
    # Территория зла

    sides = [float(input()) for _ in range(3)]
    a, b, c = sorted(sides)

    if not is_triangle(a, b, c):
        print("не треугольник")
    elif c * c > a * a + b * b:
        print("велика")
    elif c * c == a * a + b * b:
        print("100%")
    else:
        print("крайне мала")


if __name__ == "__main__":
    main()
