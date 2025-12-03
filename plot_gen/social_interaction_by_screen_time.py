import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_social_interaction_by_screen_time(df: pd.DataFrame):
    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="Screen Time per Day (Hours)",
        y="Social Interaction Score",
        hue="Stress Level",
        alpha=0.7,
        ax=ax,
    )
    ax.set_title("Social Interaction vs. Screen Time")
    ax.set_xlabel("Screen Time per Day (Hours)")
    ax.set_ylabel("Social Interaction Score")
    fig.tight_layout()
    return fig
