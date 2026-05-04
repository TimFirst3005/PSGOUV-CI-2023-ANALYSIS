import pandas as pd

from config.settings import COLUMNS

_V = COLUMNS["value"]


def total_programs(df: pd.DataFrame) -> int:
    return len(df)


def total_actions(df: pd.DataFrame) -> float:
    return df[_V].sum()


def count_unique(df: pd.DataFrame, col: str) -> int:
    return df[col].nunique()


def sum_by_col(df: pd.DataFrame, col: str) -> pd.Series:
    return df.groupby(col)[_V].sum().sort_values(ascending=False).rename(_V)


def top_n_by_cols(df: pd.DataFrame, cols: list[str], n: int = 10) -> pd.DataFrame:
    return (
        df.groupby(cols)[_V]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


def top_beneficiary(df: pd.DataFrame, col: str) -> tuple[str, float]:
    ranked = df.groupby(col)[_V].sum().sort_values(ascending=False)
    for name, value in ranked.items():
        if str(name).strip().lower() != "autres":
            return (str(name), float(value))
    return (str(ranked.index[0]), float(ranked.iloc[0]))


def treemap_data(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby([COLUMNS["district"], COLUMNS["region"], COLUMNS["category"]])[_V]
        .sum()
        .reset_index()
    )
