import requests


def main():
    # Список пользователей

    adress = "http://" + input()
    path = "/users"

    user_list = requests.get(adress + path).json()

    name_list = [user["last_name"] + " " + user["first_name"] for user in user_list]
    name_list = sorted(name_list)

    print(*name_list, sep="\n")


if __name__ == "__main__":
    main()
