import numpy as np
import pandas as pd


def values(func, start, end, step):
    # Экстремум функции

    x_values = np.arange(start=start, stop=end + step, step=step)
    func_values = map(func, x_values)
    return pd.Series(func_values, index=x_values, dtype="float64")


def min_extremum(data: pd.Series):
    return data.idxmin()


def max_extremum(data: pd.Series):
    return data.idxmax()
