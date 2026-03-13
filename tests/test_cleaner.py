import pandas as pd
from src.cleaner import clean_data

def test_clean_data():
    df = pd.DataFrame({
        "voltage": [10, 60],
        "current": [5, 2]
    })

    config = {
        "thresholds": {
            "voltage_min": 0,
            "voltage_max": 50,
            "current_min": 0,
            "current_max": 20
        }
    }

    cleaned = clean_data(df, config)
    assert len(cleaned) == 1
