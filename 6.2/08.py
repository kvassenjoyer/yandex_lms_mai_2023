import numpy as np
import pandas as pd


def update(journal: pd.DataFrame) -> pd.DataFrame:
    # Обновление журнала

    filtered = journal.copy()
    average_list = [filtered.loc[index][1:4].mean() for index in filtered.index]
    filtered = filtered.assign(average=average_list)
    filtered = filtered.sort_values(by=["average", "name"], ascending=[False, True])

    return filtered
