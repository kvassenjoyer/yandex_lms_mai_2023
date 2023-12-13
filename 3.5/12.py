import sys


def main():
    # Разделяй и властвуй

    input_filename = input()
    even_filename = input()
    odd_filename = input()
    equal_filename = input()

    with open(input_filename, "r", encoding="UTF-8") as input_file:
        for line in input_file:
            even_list, odd_list, equal_list = [], [], []

            for number_str in line.split():
                even_counter = sum([number_str.count(str(x)) for x in range(0, 9, 2)])
                odd_counter = sum([number_str.count(str(x)) for x in range(1, 10, 2)])
                if even_counter > odd_counter:
                    even_list.append(number_str)
                elif even_counter < odd_counter:
                    odd_list.append(number_str)
                else:
                    equal_list.append(number_str)

            for filename, list in zip(
                [even_filename, odd_filename, equal_filename],
                [even_list, odd_list, equal_list],
            ):
                with open(filename, "a", encoding="UTF-8") as file:
                    print(*list, file=file)


if __name__ == "__main__":
    main()
