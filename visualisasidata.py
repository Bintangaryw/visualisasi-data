import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data2.csv")
print(data.head())
print(data.info())
print(data['Team-name'].unique())


#team1 = 'Barcelona'
#print(data[data['Team-name']==team1])

unique_club = data[data.Goals>0]['Team-name'].unique()
unique_club.sort()
print(unique_club)

club_goal_case = []
for i in unique_club:
    club_goal_case.append(data[data.Goals>0][data['Team-name']==i].Goals.sum())
print(set(zip(unique_club, club_goal_case)))

unique_pemain = data['Player Name'][data.Goals>0].unique()
unique_pemain.sort()
print(unique_pemain)

pemain_goal_case = []
for i in unique_pemain:
    pemain_goal_case.append(data[data.Goals>0][data['Player Name']==i].Goals.sum())
print(set(zip(unique_pemain, pemain_goal_case)))

plt.barh(unique_club, club_goal_case)
plt.show()

plt.figure(figsize=(50,40))
plt.barh(unique_pemain, pemain_goal_case)
plt.show()

plt.figure(figsize=(10,10))
plt.pie(club_goal_case)
plt.legend(unique_club, loc="best")
plt.show

plt.figure(figsize=(20,20))
plt.pie(pemain_goal_case)
plt.legend(unique_pemain, loc='best')
plt.show