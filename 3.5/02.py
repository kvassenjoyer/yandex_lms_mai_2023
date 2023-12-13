import sys


def main():
    # Средний рост

    total_difference = 0
    pupil_amount = 0
    for line in sys.stdin:
        total_difference += abs(int(line.split()[1]) - int(line.split()[2]))
        pupil_amount += 1
    print(round(total_difference / pupil_amount))


if __name__ == "__main__":
    main()
