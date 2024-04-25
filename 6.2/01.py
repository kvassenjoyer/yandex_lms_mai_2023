import pandas as pd
import re


def length_stats(text: str):
    # Длины всех слов - 2

    # ммм, какое же четкое ТЗ - "избавьтесь от знаков препинания и цифр"
    # у меня слово "при5вет" разобьется на два слова "при" и "вет"

    words = sorted(set(re.findall(r"[a-zа-я]+", text.lower())))

    return pd.Series([len(word) for word in words], index=words)
