import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archive/Mental_Health_Dataset.csv")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Stress Level', hue='Gender', palette='muted')
plt.title('Stress Level Distribution by Gender')
plt.xlabel('Stress Level')
plt.ylabel('Count')
plt.tight_layout()
plt.show()