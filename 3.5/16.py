import sys


def main():
    # Найдётся всё 3.0

    target = input().lower()
    is_target_found = False

    filename_list = [line.strip() for line in sys.stdin]

    for filename in filename_list:
        with open(filename, "r", encoding="UTF-8") as file:
            file_content = file.read()
            file_content = ' '.join(file_content.lower().split())
            if target in file_content:
                is_target_found = True
                print(filename)

    if is_target_found is False:
        print("404. Not Found")


if __name__ == "__main__":
    main()
