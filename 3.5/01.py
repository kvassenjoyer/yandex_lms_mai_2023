import sys


def main():
    # A+B+...

    result = 0
    for line in sys.stdin:
        result += sum(map(int, line.split()))
    print(result)


if __name__ == "__main__":
    main()
