import numpy as np
import pandas as pd


def best(journal: pd.DataFrame) -> pd.DataFrame:
    # Отчёт успеваемости

    filtered = journal.copy()
    for index in journal.index:
        if not all(journal.loc[index][1:4] >= 4):
            filtered = filtered.drop([index], axis=0)

    return filtered
