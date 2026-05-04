import pandas as pd
import streamlit as st

from config.settings import COLUMNS, DATA_PATH


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    df[COLUMNS["value"]] = pd.to_numeric(df[COLUMNS["value"]], errors="coerce").fillna(0)
    return df
