#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv("datasets/gpghent.csv", sep=";")
data.describe()


#%%

# all decks
total_finishes = data['Deck'].value_counts()
# print(total_finishes)
print(total_finishes[total_finishes < 10])
#%%
# decks with 7 wins or more
top_performers = data[data['Team match points after Swiss'] >= 18]
tp = top_performers['Deck'].value_counts()[:21]
print(tp)
#print
#%%
df = pd.DataFrame({'Deck':total_finishes.index, 'Total Finishes': total_finishes.values})
df2 = pd.DataFrame({'Deck':tp.index, 'Top Finishes': tp.values})

stat_data = pd.merge(df, df2)

#%%
stat_data['Performance ratio percentage'] = stat_data['Top Finishes']/stat_data['Total Finishes']*100

#%%

plt.xticks(rotation=90)
plt.plot(stat_data['Deck'], stat_data['Total Finishes'], label='Count')
plt.plot(stat_data['Deck'], stat_data['Performance ratio percentage'], label='Performance index')
plt.legend(fontsize='x-large')

#%%
