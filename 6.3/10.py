import requests


def main():
    # Удаление данных

    adress = "http://" + input()
    path = "/users/"
    id = input()

    requests.delete(adress + path + id)


if __name__ == "__main__":
    main()
