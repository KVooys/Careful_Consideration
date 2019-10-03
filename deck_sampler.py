#%%
import os
import csv
import pprint
import random
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
# from collections import Counter

"""
Decklist format is the same as "Download" on mtggoldfish:
4 Opt
4 Path to Exile
..

<one empty line to separate maindeck & sideboard>
Sideboard:
2 Rest in Peace
2 Stony Silence
..
"""

# Given a decklist file, create an object containing the name and maindeck card list
@dataclass
class Deck:
    name: str
    cards: pd.Series = field(init=False)
    
    # List from txtfile
    def decklist(self) -> list:
        with open(os.path.join("decklists/", self.name)) as file:
            return file.readlines()
     
    # Make a list of separated cards
    def main_as_cards(self) -> pd.Series:
        decklist = self.decklist()
        split = decklist.index("\n")
        main, side = decklist[:split], decklist[split + 1:]
        cards = list()
        for card in main:
            amount, cardname = card.split(" ", 1)
            cards.extend([cardname.strip()] * int(amount))
        return pd.Series(cards, dtype=str)
    
    # Build the cardlist when loading the deck for the first time
    def __post_init__(self):
        self.cards = self.main_as_cards()
   
    # return 7 random cards
    def sample_hand(self) -> pd.Series:
        print (sorted(list(self.cards.sample(7))))
        return list(self.cards.sample(7))
     
      
# Assuming you have a directory which is filled with decklists
decklist_names = [str(f) for f in os.listdir("decklists")]


# Select a deck
current_deck = Deck("Neobrand.txt")   
# pprint.pprint(current_deck.main_as_cards())
samples = [current_deck.sample_hand() for i in range(1000)]

# store samples in a file

with open("datasets/Neobrand_1000_hands.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(samples)



#%%

# Read samples within a Pandas dataframe

data = pd.read_csv("datasets/Neobrand_1000_hands.csv")
data.columns = [int(i) for i in range(1,8)]
data.describe()


#%%
lands = ["Breeding Pool", "Botanical Sanctum", "Waterlogged Grove", "Gemstone Mine"]

# Edit dataframe to reflect lands
data2 = data.replace(lands, "Land")
data2.head()

#%%


# Next steps of data cleaning are hard.
# Manamorphose is a green card that sort of makes the deck 56 cards.
# SSG is sometimes a mana source, but not for Neoform. 
# Chancellor is always both a mana source and a green card, but the second one might not be a mana source for Neoform.
# The other green cards are just green cards, but not when they're also combo pieces (Allo, Neoform, Eldritch themselves).

# Remove 0landers for convenience
data3 = data2[data2[2] != "Land"]
data3.describe()

#%%
