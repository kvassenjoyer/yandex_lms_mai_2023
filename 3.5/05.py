import sys


def main():
    # А роза упала на лапу Азора 6.0

    palindrome_list = []
    for line in sys.stdin:
        for word in line.split():
            if word.lower() == word.lower()[::-1] and word not in palindrome_list:
                palindrome_list.append(word)

    palindrome_list.sort()
    print(*palindrome_list, sep="\n")


if __name__ == "__main__":
    main()
