import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('baseball_stats.csv')

def example_function(team_name):
	df[team_name] = df['wins']/df['runs_scored']
	team_ratio = df[df.name == team_name][['year', 'team_ratio']]
	plt.bar(team_ratio['year'], team_ratio['team_ratio'])