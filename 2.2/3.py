def main():
    # Кто быстрее на этот раз?

    name_list = ["Петя", "Вася", "Толя"]
    max_speed = -10
    answer = name_list[0]
    for i in range(len(name_list)):
        speed = int(input())
        if speed > max_speed:
            max_speed = speed
            answer = name_list[i]
    print(answer)


if __name__ == "__main__":
    main()
