#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("archive/Mental_Health_Dataset.csv")

# -------- 5 Work Hours per Week vs stress level --------

work_stress_level_low = data[data['Stress Level'] == 'Low']['Work Hours per Week'].mean()
work_stress_level_moderate = data[data['Stress Level'] == 'Moderate']['Work Hours per Week'].mean()
work_stress_level_high = data[data['Stress Level'] == 'High']['Work Hours per Week'].mean()

labels = ['Low', 'Moderate', 'High']
values = [work_stress_level_low, work_stress_level_moderate, work_stress_level_high]

plt.figure(figsize=(6,4))
bars = plt.bar(labels, values, color=['skyblue', 'orange', 'salmon'])
plt.xlabel('Stress Level')
plt.ylabel('Average Work Hours per Week')
plt.title('Average Work Hours per Week by Stress Level')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom')
plt.show()
