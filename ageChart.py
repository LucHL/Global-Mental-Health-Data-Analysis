import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "archive/Mental_Health_Dataset.csv"
df = pd.read_csv(file_path)

top_countries = df['Country'].value_counts().nlargest(6).index
filtered_df = df[df['Country'].isin(top_countries)]

plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_df, x='Country', y='Age', palette='coolwarm')
plt.title('Age Distribution by Country (Top 6)')
plt.xlabel('Country')
plt.ylabel('Age')
plt.tight_layout()
plt.show()
