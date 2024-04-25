import requests
import sys


def main():
    # Рассылка сообщений

    adress = "http://" + input()
    path = "/users/"
    id = input()

    template = ""
    for line in sys.stdin:
        template += line.strip() + "\n"

    try:
        user_dict = requests.get(adress + path + id).json()
        for key in user_dict.keys():
            template = template.replace(f"{{{key}}}", str(user_dict[key]))
        print(template)
    except ValueError:
        print("Пользователь не найден")


if __name__ == "__main__":
    main()
