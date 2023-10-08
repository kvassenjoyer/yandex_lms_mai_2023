def main():
    # В ожидании доставки

    hours = int(input())
    minutes = int(input())
    delivery_time = int(input())

    if hours in range(0, 24) and minutes in range(0, 60):
        minutes += delivery_time
        hours = (hours + minutes // 60) % 24
        minutes = minutes % 60
        print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2,'0')}")


if __name__ == "__main__":
    main()
