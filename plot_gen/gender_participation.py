import pandas as pd
from matplotlib import pyplot as plt

def get_gender_participation(df: pd.DataFrame):
    gender_sum = df["Gender"].value_counts()

    fig, ax = plt.subplots() # Create local plot
    gender_sum.plot(kind="pie", ax=ax, autopct="%1.1f%%")
    ax.set_title("Genders in dataset")
    ax.set_ylabel("")
    return fig
