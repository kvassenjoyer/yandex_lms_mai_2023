import os
import math


def main():
    # Сколько вешать в байтах?

    work_directory_path = os.path.dirname(__file__)

    relative_file_path = input()
    file_size = os.path.getsize(work_directory_path + "/" + relative_file_path)

    postfix_list = ["Б", "КБ", "МБ", "ГБ"]
    postfix_index = 0

    while file_size >= 1024 and postfix_index < len(postfix_list) - 1:
        file_size = math.ceil(file_size / 1024)
        postfix_index += 1

    print(file_size, postfix_list[postfix_index], sep="")


if __name__ == "__main__":
    main()
