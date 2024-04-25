import requests


def main():
    # Проверка системы

    response_text = requests.get("http://127.0.0.1:5000").text
    print(response_text)


if __name__ == "__main__":
    main()
