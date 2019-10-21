"""
Mythic champhionship 5 decklist analysis
Decklists parsed from https://www.mtggoldfish.com/tournament/mythic-championship-v
"""

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv("datasets/mcv_decks.csv", sep=",")
print(data.describe())


#%%

# all decks
total_finishes = data['Deck'].value_counts()

# decks with 6 wins or more are most interesting, as they represent a reasonable cutoff point
top_performers = data.loc[data['Wins']>= 6]
tp = top_performers['Deck'].value_counts()

df = pd.DataFrame({'Deck':total_finishes.index, 'Total Finishes': total_finishes.values})
df2 = pd.DataFrame({'Deck':tp.index, 'Top Finishes': tp.values})

stat_data = pd.merge(df, df2)

#%%
stat_data['Performance ratio percentage'] = stat_data['Top Finishes']/stat_data['Total Finishes']*100

#%%

plt.xticks(rotation=90)
plt.plot(stat_data['Deck'], stat_data['Total Finishes'], label='Total decks')
plt.plot(stat_data['Deck'], stat_data['Performance ratio percentage'], label='>5 wins conversion rate')
plt.legend(fontsize='x-large')


#%%
# Going a bit deeper; show wins per deck
wins_per_deck = data.groupby('Deck')
wins_per_deck.describe()

# Pretty clearly, the most popular deck was Bant Golos, but it's also very low in terms of mean wins.
# This is the result of the deck being "hated out" of the format; people were playing anti-meta decks specifically to beat it.
# For further investigation, more grouping can be done, as 4c Golos plays almost the same as Bant Golos,
# and Simic & Bant Food also play very similarly.
#%%
