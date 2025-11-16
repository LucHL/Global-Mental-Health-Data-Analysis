import pandas as pd

data = pd.read_csv("archive\Mental Health Dataset.csv")
data = data.drop(['Growing_Stress', 'Changes_Habits', 'Mood_Swings', 'Coping_Struggles', 
             'mental_health_interview', 'care_options'], axis=1)


for name, group in data.groupby('Country'):
    print(name)
    print(group)



# print(data.isnull().sum(), "\n") #check whether there is NA or not