def main():
    # Математическое форматирование

    a = int(input())
    b = int(input())
    c = int(input())

    result = (a**b) % (a + c)

    print(f"({a} ^ {b}) mod ({a} + {c}) = {result}")


if __name__ == "__main__":
    main()
