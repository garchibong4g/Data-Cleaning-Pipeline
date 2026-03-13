import os
import pandas as pd

def export_cleaned(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def export_summary(summary: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pd.DataFrame([summary]).to_csv(path, index=False)