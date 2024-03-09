import math


def main():
    # Шаг навстречу

    x_1, y_1 = [float(x) for x in input().split()]
    radius, angle = [float(x) for x in input().split()]

    x_2 = radius * math.cos(angle)
    y_2 = radius * math.sin(angle)

    distance = math.sqrt(
        math.pow(math.fabs(x_2 - x_1), 2) + math.pow(math.fabs(y_2 - y_1), 2)
    )
    print(distance)


if __name__ == "__main__":
    main()
