import pandas as pd


def get_long(data: pd.Series, min_length=5):
    # Длинные слова

    new = data.copy()
    return new[new >= min_length]
