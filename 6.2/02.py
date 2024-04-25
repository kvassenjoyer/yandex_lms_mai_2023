import pandas as pd
import re


def length_stats(text: str):
    # Длины всех слов по чётности

    word_list = sorted(set(re.findall(r"[a-zа-я]+", text.lower())))

    word_series = pd.Series([len(word) for word in word_list], index=word_list)

    return word_series[word_series % 2 == 1], word_series[word_series % 2 == 0]
