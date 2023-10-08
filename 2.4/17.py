def main():
    # А роза упала на лапу Азора 3.0
    
    n = int(input())
    counter = 0
    for _ in range(n):
        number = input()
        if number == number[::-1]:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
