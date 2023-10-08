def main():
    # А роза упала на лапу Азора 5.0

    expression = input()
    expression = expression.replace(" ", "").lower()
    if expression == expression[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
