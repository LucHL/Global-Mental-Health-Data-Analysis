import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_age_participation(df: pd.DataFrame):
    top_countries = df["Country"].value_counts().nlargest(6).index
    filtered_df = df[df["Country"].isin(top_countries)]

    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, x="Country", y="Age", ax=ax, hue="Country", palette="coolwarm")
    ax.set_title("Age Distribution by Country (Top 6)")
    ax.set_xlabel("Country")
    ax.set_ylabel("Age")
    fig.tight_layout()
    return fig
