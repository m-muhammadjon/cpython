import pandas as pd


def gt_mean(series: pd.Series) -> pd.Series:
    oa = sum(series.array) / len(series.array)
    print(series.compare(pd.Series(oa)))
    return pd.Series([item for item in series.array if item > oa])


series = pd.Series([1, 5, 2, 3, 4])
print(gt_mean(series))

