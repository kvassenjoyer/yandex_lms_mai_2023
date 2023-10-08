def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    flag = True
    for divider in range(3, int(number**0.5) + 2, 2):
        if number % divider == 0:
            flag = False
    return flag


def main():
    # Простая задача

    number = int(input())
    if is_prime(number):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
