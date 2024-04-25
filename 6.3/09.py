import requests
import sys


def main():
    # Изменение данных

    adress = "http://" + input()
    path = "/users/"
    id = input()

    updated_user_data = {}

    for line in sys.stdin:
        key, value = line.strip().split("=")
        updated_user_data[key] = value

    requests.put(adress + path + id, json=updated_user_data)


if __name__ == "__main__":
    main()
