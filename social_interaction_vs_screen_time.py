import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archive/Mental_Health_Dataset.csv")

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x='Screen Time per Day (Hours)',
    y='Social Interaction Score',
    hue='Stress Level',
    alpha=0.7
)
plt.title('Social Interaction vs. Screen Time')
plt.xlabel('Screen Time per Day (Hours)')
plt.ylabel('Social Interaction Score')
plt.tight_layout()
plt.show()