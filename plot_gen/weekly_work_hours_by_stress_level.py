import pandas as pd
import matplotlib.pyplot as plt

def get_weekly_work_hours_by_stress_level(df: pd.DataFrame):
    work_stress_level_low = df[df["Stress Level"] == "Low"]["Work Hours per Week"].mean()
    work_stress_level_moderate = df[df["Stress Level"] == "Moderate"]["Work Hours per Week"].mean()
    work_stress_level_high = df[df["Stress Level"] == "High"]["Work Hours per Week"].mean()

    labels = ["Low", "Moderate", "High"]
    values = [work_stress_level_low, work_stress_level_moderate, work_stress_level_high]

    fig, ax = plt.subplots()
    bars = plt.bar(labels, values, color=["skyblue", "orange", "salmon"])
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Average Work Hours per Week")
    ax.set_title("Average Work Hours per Week by Stress Level")
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}", ha="center", va="bottom")
    return fig
