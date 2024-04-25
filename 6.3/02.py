import requests


def main():
    # Суммирование ответов

    adress = "http://" + input()
    
    response_number = None
    result_sum = 0
    while response_number != 0:
        response_number = int(requests.get(adress).text)
        result_sum += response_number

    print(result_sum)


if __name__ == "__main__":
    main()
