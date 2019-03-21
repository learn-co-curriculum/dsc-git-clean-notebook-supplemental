import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('baseball_stats.csv')

def example_function(name):
    df['team_ratio'] = df['wins']/df['runs_scored']
    team_ratio = df[df.name == 'Arizona Diamondbacks'][['year', 'team_ratio']]
    plt.bar(team_ratio['year'], team_ratio['team_ratio'])
    