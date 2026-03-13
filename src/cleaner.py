import pandas as pd

def clean_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    thresholds = config["thresholds"]

    df = df.copy()

    # Drop missing values
    df.dropna(inplace=True)

    # Filter based on thresholds
    df = df[
        (df["voltage"].between(thresholds["voltage_min"], thresholds["voltage_max"])) &
        (df["current"].between(thresholds["current_min"], thresholds["current_max"]))
    ]

    return df