import numpy as np
import pandas as pd


def main():
    # Бесконечный морской бой

    field = pd.read_csv("data.csv")

    x_min, y_max = map(int, input().split())
    x_max, y_min = map(int, input().split())

    field = field[
        (field["x"] >= x_min)
        & (field["x"] <= x_max)
        & (field["y"] >= y_min)
        & (field["y"] <= y_max)
    ]
    print(field)


if __name__ == "__main__":
    main()
