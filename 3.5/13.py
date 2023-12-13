import json
import sys


def main():
    # Обновление данных

    output_filename = input()

    with open(output_filename, 'r', encoding="UTF-8") as output_file:
        data = json.load(output_file)
        
    for line in sys.stdin:
        key, value = line.strip().split(" == ")
        data[key] = value

    with open(output_filename, "w", encoding="UTF-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
