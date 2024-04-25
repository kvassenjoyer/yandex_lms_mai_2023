import numpy as np
import pandas as pd


def need_to_work_better(journal: pd.DataFrame) -> pd.DataFrame:
    # Отчёт неуспеваемости

    filtered = journal.copy()
    for index in journal.index:
        if not any(journal.loc[index][1:4] == 2):
            filtered = filtered.drop([index], axis=0)

    return filtered
