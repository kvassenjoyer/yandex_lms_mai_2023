def main():
    # Зайка — 2

    target = "зайка"
    lines = [input() for _ in range(3)]
    lines = sorted(lines)

    for line in lines:
        if target in line:
            print(line, len(line))
            break


if __name__ == "__main__":
    main()
