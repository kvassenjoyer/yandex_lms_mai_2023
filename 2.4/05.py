def main():
    # Зайка — 5

    n = int(input())
    target = "зайка"
    result = 0
    for _ in range(n):
        flag = False
        word = "Я сказала стартуем"
        while word != "ВСЁ":
            word = input()
            if word == target:
                flag = True
        if flag:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
