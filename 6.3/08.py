import requests


def main():
    # Регистрация нового пользователя

    adress = "http://" + input()
    path = "/users"

    user_dict = {
        "username": input(),
        "last_name": input(),
        "first_name": input(),
        "email": input(),
    }
    requests.post(adress + path, json=user_dict)


if __name__ == "__main__":
    main()
