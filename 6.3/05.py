import requests
import sys


def main():
    # Суммирование ответов 3

    adress = "http://" + input()

    path_list = [path.strip() for path in sys.stdin]

    result_sum = 0
    for path in path_list:
        response_list = requests.get(adress + path).json()
        result_sum += sum([x for x in response_list if type(x) in [int, float]])

    print(result_sum)


if __name__ == "__main__":
    main()
