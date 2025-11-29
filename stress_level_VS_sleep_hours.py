#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("archive/Mental_Health_Dataset.csv")

# -------- 1 Stress level vs. Sleep hours --------

sleep_low = data[data['Stress Level'] == 'Low']['Sleep Hours'].mean()
sleep_moderate = data[data['Stress Level'] == 'Moderate']['Sleep Hours'].mean()
sleep_high = data[data['Stress Level'] == 'High']['Sleep Hours'].mean()

labels = ['Low', 'Moderate', 'High']
values = [sleep_low, sleep_moderate, sleep_high]

plt.figure(figsize=(6,4))
bars = plt.bar(labels, values, color=['skyblue', 'orange', 'salmon'])
plt.xlabel('Stress Level')
plt.ylabel('Average Sleep Hours')
plt.title('Average Sleep Hours by Stress Level')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom')
plt.show()
