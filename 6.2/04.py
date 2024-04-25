import numpy as np
import pandas as pd


def discount(data: pd.DataFrame):
    # Акция 

    new = data.copy()
    new["cost"] = np.where(new["number"] > 2, 0.5 * new["cost"], new["cost"])
    return new


def cheque(price_list: pd.Series, **kwargs):
    kwargs = dict(sorted(kwargs.items()))
    return pd.DataFrame(
        {
            "product": kwargs.keys(),
            "price": [price_list[key] for key in kwargs.keys()],
            "number": kwargs.values(),
            "cost": [value * price_list[key] for key, value in kwargs.items()],
        }
    )
