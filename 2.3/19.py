def main():
    # Игра в «Угадайку»

    left_border, right_border = 0, 1001
    feedback = ""
    while feedback != "Угадал!":
        guess = (right_border + left_border) // 2
        print(guess)
        feedback = input()
        if feedback == "Больше":
            left_border = guess
        elif feedback == "Меньше":
            right_border = right_border - (right_border - left_border) // 2


if __name__ == "__main__":
    main()
