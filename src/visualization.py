import matplotlib.pyplot as plt
import pandas as pd

def plot_power(df: pd.DataFrame, path: str):
    plt.figure()
    plt.plot(df["time"], df["power"])
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.title("Power vs Time")
    plt.savefig(path)
    plt.close()