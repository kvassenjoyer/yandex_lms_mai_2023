def main():
    # Азбука
    
    n = int(input())

    flag = True
    for _ in range(n):
        word = input()
        first_char = word[0]
        if first_char not in "абв":
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
