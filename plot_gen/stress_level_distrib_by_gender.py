import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_stress_level_distrib_by_gender(df: pd.DataFrame):
    fig, ax = plt.subplots()

    sns.countplot(data=df, x="Stress Level", hue="Gender", palette="muted", ax=ax)

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Stress Level Distribution by Gender")
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig
