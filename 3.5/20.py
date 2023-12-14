def main():
    # Файловая сумма

    with open("numbers.num", "rb") as file:
        data = file.read()

    result = 0
    for i in range(0, len(data), 2):
        result += int.from_bytes(data[i: i + 2], "big")
    result = result % 2**16

    print(result)


if __name__ == "__main__":
    main()
