import pandas as pd

def compute_features(df):
    if df.empty:
        return None
    if df["value"].isnull().any():
        raise ValueError("Null values detected")
    return {
        "mean_value": float(df["value"].mean()),
        "sum_value": float(df["value"].sum())
    }
