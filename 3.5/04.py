import sys


def main():
    # Найдётся всё 2.0

    line_list = []
    for line in sys.stdin:
        line_list.append(line.strip())

    if len(line_list) != 0:
        target = line_list[-1]
        line_list.pop(-1)

    for line in line_list:
        if target.lower() in line.lower():
            print(line)

            
if __name__ == "__main__":
    main()
