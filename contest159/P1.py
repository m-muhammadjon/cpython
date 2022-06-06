import pandas as pd


def lowercase_letters() -> pd.Series:
    return pd.Series(range(1, 27), index=list('abcdefghijklmnopqrstuvwxyz'))


s = lowercase_letters()
print(s['a'])
