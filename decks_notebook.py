#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv("datasets/mciv_decks.csv", sep=";")
print(data.describe())


#%%

# all decks
total_finishes = data['Deck'].value_counts()

# decks with 6 wins or more have their result noted as a number instead of a -
top_performers = data.loc[data['Wins']!= '-']
tp = top_performers['Deck'].value_counts()

df = pd.DataFrame({'Deck':total_finishes.index, 'Total Finishes': total_finishes.values})
df2 = pd.DataFrame({'Deck':tp.index, 'Top Finishes': tp.values})

stat_data = pd.merge(df, df2)

#%%
stat_data['Performance ratio percentage'] = stat_data['Top Finishes']/stat_data['Total Finishes']*100

#%%

plt.xticks(rotation=90)
plt.plot(stat_data['Deck'], stat_data['Total Finishes'], label='Total decks')
plt.plot(stat_data['Deck'], stat_data['Performance ratio percentage'], label='Performance')


#%%
