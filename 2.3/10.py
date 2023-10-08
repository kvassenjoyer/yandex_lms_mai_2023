def main():
    # Маршрут построен

    x, y = 0, 0
    direction = ""
    while direction != "СТОП":
        direction = input()
        if direction != "СТОП":
            steps = int(input())
        if direction == "СЕВЕР":
            y += steps
        elif direction == "ЮГ":
            y -= steps
        elif direction == "ЗАПАД":
            x -= steps
        elif direction == "ВОСТОК":
            x += steps
    print(y)
    print(x)


if __name__ == "__main__":
    main()
