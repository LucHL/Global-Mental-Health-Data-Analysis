import pandas as pd
import matplotlib.pyplot as plt

def get_stress_level_by_sleep_hours(df: pd.DataFrame):
    sleep_low = df[df["Stress Level"] == "Low"]["Sleep Hours"].mean() # Get mean of sleep hours only for low stress level
    sleep_moderate = df[df["Stress Level"] == "Moderate"]["Sleep Hours"].mean() # Same but for moderate stress level
    sleep_high = df[df["Stress Level"] == "High"]["Sleep Hours"].mean() # Same but for high stress level
    
    labels = ["Low", "Moderate", "High"]
    values = [sleep_low, sleep_moderate, sleep_high]

    fig, ax = plt.subplots() # Create local plot

    bars = plt.bar(labels, values, color=["skyblue", "orange", "salmon"])
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Average Sleep Hours")
    ax.set_title("Average Sleep Hours by Stress Level")
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}", ha="center", va="bottom")
    return fig
