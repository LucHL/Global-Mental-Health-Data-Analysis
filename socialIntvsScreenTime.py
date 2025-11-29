import pandas as pd
import matplotlib.pyplot as plt

file_path = 'archive/Rounded_Modified_Mental_Health_Dataset.csv'
df = pd.read_csv(file_path)

screen_col = 'Screen Time per Day (Hours)'
social_col = 'Social Interaction Score'

df['Screen_Time_Hours_Rounded'] = df[screen_col].round().astype(int)

avg_data = df.groupby('Screen_Time_Hours_Rounded')[social_col].mean().reset_index()

avg_data = avg_data.sort_values('Screen_Time_Hours_Rounded')

plt.figure()
plt.plot(avg_data['Screen_Time_Hours_Rounded'], avg_data[social_col], marker='o')
plt.xlabel("Screen Time (Rounded to Hours)")
plt.ylabel("Average Social Interaction Score")
plt.title("Average Social Interaction vs Screen Time (Hourly Buckets)")
plt.tight_layout()
plt.show()
