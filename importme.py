import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/utaveras/FlatironSchool/DS-031119/Week2/Day4/dsc-git-clean-notebook-supplemental/baseball_stats.csv')

teams = df.name.unique()

df['team_ratio'] = df['wins']/df['runs_scored']

team_ratio = df[df.name == 'Arizona Diamondbacks'][['year', 'team_ratio']]

plt.bar(team_ratio['year'], team_ratio['team_ratio'])
