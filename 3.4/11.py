def main():
    # Числовой прямоугольник 3.0

    n = int(input())
    m = int(input())

    element_width = len(str(n * m))
    for line_index in range(n):
        line_start = line_index * m + 1
        line = range(line_start, line_start + m)
        print(*map(lambda x: str(x).rjust(element_width), line))


if __name__ == "__main__":
    main()
