def main():
    # Странный калькулятор

    a = int(input())
    expression = input()
    b = int(input())
    result = None

    if len(expression) % 2 == 0:
        if " " in expression:
            result = a + b
        else:
            result = a - b
    else:
        if " " in expression:
            result = a * b
        else:
            result = a // b
    print(result)


if __name__ == "__main__":
    main()
