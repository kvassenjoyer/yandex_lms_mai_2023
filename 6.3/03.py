import requests


def main():
    # Суммирование ответов 2

    adress = "http://" + input()

    response_list = requests.get(adress).json()

    result_sum = sum([x for x in response_list if type(x) in [int, float]])

    print(result_sum)


if __name__ == "__main__":
    main()
    