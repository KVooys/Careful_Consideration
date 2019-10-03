# Careful Consideration

![Careful Consideration](https://media.wizards.com/2015/images/daily/cardart_CarefulConsideration.jpg)

Repository for using data analytics to improve my Magic: the Gathering decision game, while learning data tech as a side effect.

I've done this in a couple different ways:

- deck_sampler.py takes a decklist and generates a lot of opening hands, then it does some statistical analysis on that to see if the manabase is adequate, for instance.
- decks_notebook.py is a Jupyter Notebook to analyze deck performance in a large tournament; it takes some tournament results and some way to determine performance (I used day 2 percentage) and then makes nice stats and graphs out of them.

An example result from gp_ghent_results_notebook.py:

![GP Ghent performance index](https://github.com/KVooys/Careful_Consideration/blob/master/gp_ghent_sample.png)
