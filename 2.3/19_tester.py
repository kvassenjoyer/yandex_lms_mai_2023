def tester(secret, guess):
    # Игра в «Угадайку»
    if secret < guess:
        feedback = "Меньше"
    elif secret > guess:
        feedback = "Больше"
    else:
        feedback = "Угадал!"
    return feedback


def guesser(secret):
    counter = 0  # добавлено для тестирования
    left_border, right_border = 0, 1001
    feedback = ""
    while feedback != "Угадал!" and counter < 15:  # counter добавлен для тестирования
        counter += 1  # добавлено для тестирования
        guess = (right_border + left_border) // 2
        # print(guess) # убрано для автоматического тестирования
        # print(guess, left_border, right_border) # добавить для более подробного тестирования
        feedback = tester(secret, guess)
        if feedback == "Больше":
            left_border = guess
        elif feedback == "Меньше":
            right_border = right_border - (right_border - left_border) // 2
    return counter, secret  # добавлено для тестирования


def main():
    max_tries = 0
    max_tries_number = 1
    for secret in range(1, 1001):
        current, number = guesser(secret)
        if current > max_tries:
            max_tries = current
            max_tries_number = number
    print(max_tries, max_tries_number)


if __name__ == "__main__":
    main()
