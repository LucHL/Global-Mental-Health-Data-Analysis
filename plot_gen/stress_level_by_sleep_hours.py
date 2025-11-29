import pandas as pd
import matplotlib.pyplot as plt

def get_stress_level_by_sleep_hours(df: pd.DataFrame):
    sleep_low = df[df["Stress Level"] == "Low"]["Sleep Hours"].mean()
    sleep_moderate = df[df["Stress Level"] == "Moderate"]["Sleep Hours"].mean()
    sleep_high = df[df["Stress Level"] == "High"]["Sleep Hours"].mean()
    
    labels = ["Low", "Moderate", "High"]
    values = [sleep_low, sleep_moderate, sleep_high]

    fig, ax = plt.subplots()

    bars = plt.bar(labels, values, color=["skyblue", "orange", "salmon"])
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Average Sleep Hours")
    ax.set_title("Average Sleep Hours by Stress Level")
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}", ha="center", va="bottom")
    return fig
