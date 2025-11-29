import pandas as pd
from matplotlib import pyplot as plt

def get_gender_participation(df: pd.DataFrame):
    gender_sum = df["Gender"].value_counts()

    fig, ax = plt.subplots()
    gender_sum.plot(kind="pie", ax=ax)
    ax.set_title("Genders in dataset")
    ax.set_ylabel("")
    return fig

get_gender_participation(pd.read_csv("archive/Mental_Health_Dataset.csv"))
