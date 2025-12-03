import pandas as pd
from matplotlib import pyplot as plt

def get_country_participation(df: pd.DataFrame):
    country_sum = df["Country"].value_counts()

    fig, ax = plt.subplots()
    country_sum.plot(kind="pie", ax=ax, autopct="%1.1f%%")
    ax.set_title("Countries in dataset")
    ax.set_ylabel("")
    return fig
