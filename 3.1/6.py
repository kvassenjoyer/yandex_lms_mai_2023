def main():
    # Зайка — 6
    
    n = int(input())
    target = "зайка"
    result = 0
    for _ in range(n):
        line = input()
        result += line.count(target)
    print(result)


if __name__ == "__main__":
    main()
