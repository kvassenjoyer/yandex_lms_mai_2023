def main():
    # Просто здравствуй, просто как дела

    name = input("Как Вас зовут?\n")
    print(f"Здравствуйте, {name}!")

    status = input("Как дела?\n")
    if status == "хорошо":
        print("Я за вас рада!")
    elif status == "плохо":
        print("Всё наладится!")
    else:
        print("Я вас не понимаю.")


if __name__ == "__main__":
    main()
