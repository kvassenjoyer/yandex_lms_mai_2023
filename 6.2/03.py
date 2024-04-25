import pandas as pd


def cheque(price_list: pd.Series, **kwargs):
    # Чек - 2

    kwargs = dict(sorted(kwargs.items()))
    return pd.DataFrame(
        {
            "product": kwargs.keys(),
            "price": [price_list[key] for key in kwargs.keys()],
            "number": kwargs.values(),
            "cost": [value * price_list[key] for key, value in kwargs.items()],
        }
    )
