def main():
    # Зайка — 7
    
    n = int(input())
    target = "зайка"
    for _ in range(n):
        line = input()
        result = line.find(target)
        if result == -1:
            print("Заек нет =(")
        else:
            print(result + 1)


if __name__ == "__main__":
    main()
