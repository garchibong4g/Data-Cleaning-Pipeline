import pandas as pd

def compute_power(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["power"] = df["voltage"] * df["current"]
    return df

def generate_summary(df: pd.DataFrame) -> dict:
    return {
        "mean_power": df["power"].mean(),
        "max_power": df["power"].max(),
        "min_power": df["power"].min(),
        "std_power": df["power"].std()
    }