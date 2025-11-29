import pandas as pd
from matplotlib import pyplot as plt

def get_country_participation(df: pd.DataFrame):
    country_sum = df["Country"].value_counts()

    fig, ax = plt.subplots()
    country_sum.plot(kind="pie", ax=ax)
    ax.set_title("Countries in dataset")
    ax.set_ylabel("")
    return fig

get_country_participation(pd.read_csv("archive/Mental_Health_Dataset.csv"))
