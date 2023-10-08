def get_nod(a, b):
    while a != 0:
        if b < a:
            a, b = b, a
        a, b = b - a, a
    return b


def main():
    # НОД 2.0
    
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    result = get_nod(numbers[0], numbers[1])
    for i in range(2, n):
        result = get_nod(result, numbers[i])
    print(result)


if __name__ == "__main__":
    main()
