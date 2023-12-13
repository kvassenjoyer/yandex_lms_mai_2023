import sys


def main():
    # Без комментариев 2.0

    for line in sys.stdin:
        if line.find("#") != 0:
            print(line[: line.find("#")])


if __name__ == "__main__":
    main()
