import math


def main():
    # Есть варианты?

    N, M = [int(x) for x in input().split()]
    print(math.comb(N, M) - math.comb(N - 1, M), math.comb(N, M))


if __name__ == "__main__":
    main()
