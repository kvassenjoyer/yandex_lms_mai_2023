def main():
    # Детский сад — штаны на лямках

    name = input()
    locker = int(input())

    print(f"Группа №{locker//100}.")
    print(f"{locker%10}. {name}.")
    print(f"Шкафчик: {locker}.")
    print(f"Кроватка: {locker%100//10}.")


if __name__ == "__main__":
    main()
