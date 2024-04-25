import requests


def main():
    # Конкретное значение

    adress = "http://" + input()
    key = input()

    response_dict = requests.get(adress).json()

    if key in response_dict.keys():
        print(response_dict[key])
    else:
        print("No data")


if __name__ == "__main__":
    main()
